
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn="
l = list()
for page in  range(1,2) : 

    html_text = requests.get(URL + str(page) + "#catalog-listing").content

    soup = bs(html_text,'html.parser')

    produits = soup.find_all('li', class_ ="s-item s-item__pl-on-bottom s-item--watch-at-corner")
    for prod in produits :
        info = prod.find("div",class_ ="s-item__info clearfix")  

        link = info.find("a", class_='s-item__link').attrs['href']
        
        html_text2 = requests.get(link).content
        soup2 = bs(html_text2,'html.parser')

        try :
            title = soup2.find('h1', class_='x-item-title__mainTitle').text
        except :
            title =" undefind "  
        try :
            price= soup2.find('span', class_="notranslate").text    
        except :
            price =" undefind "
        
        try :
            sold = soup2.find('a', class_='vi-txt-underline').text
        except :
            sold =" undefind "
        try :
            available = soup2.find('span', id='qtySubTxt').text
        except :
            available =" undefind "
        try :
            delivry = soup2.find('div', class_='w2b-cnt w2b-3 w2b-red').text
        except :
            delivry =" undefind "

        try :
            location = soup2.find('div', id='itemLocation').text
        except :
            location =" undefind "
            
        data = {"Title":title, "Price":price, "Sold":sold, "Available":available ,"Delivry":delivry, "Location":location }
                
        l.append(data)
        #print(data)

 ##            Storing in Excel File    ##
df = pd.DataFrame(l)
df.to_excel("/Users/Pro/Documents/Master MBD/MBD_S2/Web-Scraping/Ebay_Scrap/EbayTest.xlsx")

##        Storing in MongoDb       ##

# from pymongo import MongoClient

# client = MongoClient()
# client = MongoClient('localhost', 27017 )

# db = client.get_database('ebay')

# for produit in l :
#     db.get_collection('ebayCollection').insert_one(produit)


#print(df.tail())

