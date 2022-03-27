
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn="
l = list()
for page in  range(1,5) : 

    html_text = requests.get(URL + str(page) + "#catalog-listing").content

    soup = bs(html_text,'html.parser')

    produits = soup.find_all('li', class_ ="s-item s-item__pl-on-bottom s-item--watch-at-corner")

    for prod in produits :
        info = prod.find("div",class_ ="s-item__info clearfix")  
     
        try :
            title = info.find('a', class_='s-item__link').text
        except:
            title =''   
        try :
            price= info.find('span', class_="s-item__price").text 
        except:
            price =''
        
        detail= info.find('div', class_='s-item__details clearfix')

        try :
            sold = detail.find('span', class_='s-item__hotness s-item__itemHotness').text
        except:
            sold ='0 sold'
        try :
            delivry = detail.find('span', class_='s-item__shipping s-item__logisticsCost').text
        except:
            delivry =''
        
        try :
            country = detail.find('span', class_='s-item__location s-item__itemLocation').text
        except:
            country =''

        data = {"Title":title, "Country":country, "Price":price, "Sold":sold,"Delivry":delivry }
                
        l.append(data)
      #  print(data)

 # Storing in Excel File   
# df = pd.DataFrame(l)
# df.to_excel("/Users/Pro/Documents/Master MBD/MBD_S2/Web-Scraping/Ebay_Scrap/ebay.xlsx")

# Storing in MongoDb  

from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017 )

db = client.get_database('ebay')

for produit in l :
    db.get_collection('ebayCollection').insert_one(produit)


#print(df.tail())

