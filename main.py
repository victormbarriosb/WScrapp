from pip._vendor import requests
from bs4 import BeautifulSoup
#Web Scrap Para Productos, Precios, Nombre, Marca, y Codigos de Barras

#CheckPointSystem
Archivo = open("UrlSectores.txt", "w")


# Carga de Urls a Categorias
page = requests.get("https://www.superseis.com.py/default.aspx")
soup = BeautifulSoup(page.content, 'html.parser')
MenuDesplegable = soup.find(class_="catnav wstabitem clearfix")
inactive_evel1 = MenuDesplegable.find_all(class_="inactive level1")
for x in inactive_evel1:
  SectorTitulo = x.find(class_="collapsed").text
  #print("% 2s" %(SectorTitulo))
  inactive_level2 = x.find_all(class_="inactive level2")
  for y in inactive_level2:
    SubSectorTitulo = y.find(class_="collapsed").text
    #print("- % 2s" % (SubSectorTitulo))
    inactive_level3 = y.find_all(class_="inactive level3")
    for z in inactive_level3:
      TipoTitulo = z.find(class_="collapsed").text
      link = z.find('a', href=True)
      if link is None:
        continue
      TipoLink = link['href']
      #Archivo.write("%s: %s \n" % (TipoTitulo,TipoLink))
      print("-- % 2s" % (TipoTitulo))
      print("--- % 2s" % (TipoLink))

#Archivo.close()





#ArchivoBD = open("UrlSectores.txt", "r+")
#with open("UrlSectores.txt", 'r') as f:
 # for line in f:
  #  print(line)
   # if 'str' in line:
     # break