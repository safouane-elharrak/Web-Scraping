
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.mubawab.ma/fr/cc/immobilier-a-vendre:p:3"
l = list()
for page in  range(1, 2) : 

    html_text = requests.get(URL + str(page) + "#catalog-listing").content

    soup = bs(html_text,'html.parser')
    ###            Partie Links             ###
    links = soup.find_all('li',class_='listingBox w100')
    for cont in links :
        try :
            title = cont.find('h2', class_='listingTit')
        except :
            title = 'walu'

        try :
            link = title.find('a').attrs['href']
        except :
            link = 'walu'

        ###      Partie Liaison                  ###

        html_text2 = requests.get(link).content
        soup2 = bs(html_text2,'html.parser')
        
        ###       Partie Content                 ###
        content = soup2.find('div', class_='bottomContainer')
        photos = content.find_all('div', class_='bottomPicture')
        for photo in photos:
            try:
                picture = photo.find('img').attrs['src']
            except :
                picture = 'not defined'

        content2 = soup2.find('section', class_='propPage')

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
        print (title)
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

        l.append(data)





#  # Storing in Excel File   
# df = pd.DataFrame(l)
# df.to_excel("/Users/Pro/Documents/Master MBD/MBD_S2/Web-Scraping/Mubawab_Vente/mubawab.xlsx")

# Storing in MongoDb  

# from pymongo import MongoClient

# client = MongoClient()
# client = MongoClient('localhost', 27017 )

# db = client.get_database('Mubawab')

# for produit in l :
#     db.get_collection('MubawabCollection').insert_one(produit)


#print(df.tail())

