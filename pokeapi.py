from google.colab import drive
drive.mount('/content/drive')

import requests as rq
from bs4 import BeautifulSoup
import datetime
import pathlib
import re
from google.colab import drive
import urllib

def agregar_pokemon(poke):
 base_url = "https://pokeapi.co/api/v2/pokemon/" + poke
 response = rq.get(base_url)
 soup = BeautifulSoup(str(response.content),"html.parser")
 soup2=str(soup).replace("[","\t <div class=")
 soup2=str(soup2).replace("]","</div>\n")
 soup2=str(soup2).replace(",{","<div class=")
 soup2=str(soup2).replace(',','</div><div class=')
 soup2=str(soup2).replace('{',"")
 soup2=str(soup2).replace("name"," ")
 soup2=str(soup2).replace('\" \"',"")
 soup2=str(soup2).replace("}","</div> \n")
 soup2=str(soup2).replace('":','">')
 soup2=str(soup2).replace('>:','>')
 soup2=BeautifulSoup(soup2,"html.parser")
 result = soup2.findAll(attrs={'class': re.compile(r"base_experience")})
 result1 = soup2.findAll(attrs={'class': re.compile(r"id")})
 result2 = soup2.findAll(attrs={'class': re.compile(r'stat')})
 result3 = soup2.findAll(attrs={'class': re.compile(r"ability")})
 resultante= '\n' + str(dato) + " " + str(datetime.datetime.now()) + ",\n" + "id: " + str(result1)+"\n base_experience: "+str(result)+"\n stat: "+str(result2)+"\n abilities: "+str(result3)
 soup=str(resultante).replace('div class=','')
 soup=str(soup).replace('</div>','')
 soup=str(soup).replace(',','\t')
 soup=str(soup).replace('"',"")
 soup=str(soup).replace('<','')
 soup=str(soup).replace('>','=')
 #print("Estas Escribiendo:",str(soup))
 archivo=open('/content/drive/MyDrive/Colab Notebooks/history.csv','a')
 archivo.write('\n' + str(soup))
 archivo.close()
 mostrar_registro(poke)

def mostrar_registro(poke):
 archivo=open('/content/drive/MyDrive/Colab Notebooks/history.csv','r')
 print(archivo.read())
 archivo.close()
 print("Do you like to see the complete data? : \n")
 choice=input("y/n: ")
 count=0
 if choice == 'y':
  archivo=open('/content/drive/MyDrive/Colab Notebooks/history.csv','r')
  try:
   print('Mostrando los primeros 20 registros')
   for linea in archivo:
    if count < 21:
      print(linea)
      count=count + 1
    else:
      input('presiona una tecla para continuar')
      print('Mostrando otros 20 registros')
      count=0
  finally:
   archivo.close()
 else:
  print("Saliendo..")

if __name__ == "__main__":
 print('Busqueda en pokeapi.com: \n ')
 flag=0
 dato = input('Escribe el nombre del pokemon a buscar: ')
 
 
 file = pathlib.Path("/content/drive/MyDrive/Colab Notebooks/history.csv")
 if file.exists ():
    print ("")
 else:
    file.touch()
 history2=open("/content/drive/MyDrive/Colab Notebooks/history.csv",'r')
 existent=history2.readlines()
 for line in existent:
    palabras = line.split(' ')
    for p in palabras:
        if p==dato:
            flag = 1
 history2.close()
 
 if flag==1:
  with open("/content/drive/MyDrive/Colab Notebooks/history.csv","r") as f:
   nuevo=dato+"............................"
   nuevo3=str(dato) + " " + str(datetime.datetime.now()) + ","
   nuevo2=re.sub(nuevo, nuevo3,f.read())
  with open("/content/drive/MyDrive/Colab Notebooks/history.csv", 'w') as f:
   f.write(nuevo2)
  f.close()
  print("Pokemon registrado Anteriormente")
  mostrar_registro(dato)
 else:
  print("Agregando Nuevo Pokemon: ",dato)
  agregar_pokemon(dato)
