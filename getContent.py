
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.mubawab.ma/fr/a/7395211/nouveau-projet-somptueuses-villas-500-m%C2%B2"
l = list()


html_text = requests.get(URL + "#catalog-listing").content

soup = bs(html_text,'html.parser')

content = soup.find('div', class_='bottomContainer')

photos = content.find_all('div', class_='bottomPicture')

for photo in photos:
    try:
        picture = photo.find('img').attrs['src']
    except :
        picture = 'not defined'

content2 = soup.find('section', class_='propPage')

#title = content2.find('h1', class_='searchTitle').text
# price = content2.find('h3', class_='orangeTit').text
# ville = content2.find('h3', class_='greyTit').text
#pieces = content2.find('div', class_='catNav').text
#description = content2.find('div', class_='blockProp').find('p').text
caracteres = content2.find_all('li', class_='col-2 floatR fSize14')

for carac in caracteres:
    try:
        caractere = carac.find('span',class_='characIconText centered').text
    except :
        caractere = 'not defined'
try :
    title = content2.find('h1', class_='searchTitle').text 
except:
    title = 'not defined'

try:
    price = content2.find('h3', class_='orangeTit').text
except:
    price = 'not defined'

try :
    ville = content2.find('h3', class_='greyTit').text
except:
    ville = 'not defined'

try :
    pieces = content2.find('div', class_='catNav').text
except:
    pieces = 'not defined'

try :
    description = content2.find('div', class_='blockProp').find('p').text
except:
    description = 'not defined'


data = {"Title":title, "Location":ville, "Price":price, "Caractéristiques":caractere,"Mobilier":pieces,"Description":description,"Pictures":picture}
print(data)

l.append(data)

