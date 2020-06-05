from bs4 import BeautifulSoup
from flask import Flask
from flaskext.mysql import MySQL
import constants
import requests
import time 
import json

def getLinks():
    links = []
    #get all the links from multiple page
    i = constants.FirstPage 
    max = constants.NumberofPages
    while i <= max:
        j = str(i)
        raw = souped(constants.baseURL+j)
        time.sleep(30)
        findlink = raw.findAll('div', class_='gallery-container')
        for div in findlink:
            r = div.a['href']
            links.append(r)
            # print(links)
        i+=1
    print(links)
    print(len(links))
    time.sleep(60)
    return links



def souped(url):
    #ensure all request being proxied to avoid CAPTCHA
    temp = requests.get(url,headers = constants.header , proxies = constants.proxies)
    soup = BeautifulSoup(temp.text, 'html.parser')
    return soup


def getData(url):
    #grab Real Estate Data From All Links
    
    data = {'list':[{}]}
    i = 0

    #for i in url :
    while i < 4 : 
        grabbed = {'link' : '','name' : '','type' : '','price' : '','address' : '','built_up': '','land_area' : '',
        'bedrooms' : '','bathrooms' : '','monthly_installment' : '','land_title' : '','tenure' : '', 'price_per_sqft' : '','maintenance_fee' : 0,'furnishing' : '','state' : ''}

        time.sleep(60)
        soup = souped(url[i])
        print(soup.h1.text)

        soupp = soup.findAll('div',class_='property-attr')
        
        #link
        grabbed['link'] = url[i]

        #name 
        grabbed['name'] = soup.h1.text

        #type
        grabbed['type'] = soupp[0].find('div',itemprop='value').text

        #price
        tempprice = soup.find('span',class_='element-label price').text.strip()
        tempprice = tempprice.replace(',','') 
        tempprice = tempprice.replace('RM ','')
        grabbed['price'] = int(tempprice)

        #address
        grabbed['address'] = soup.find('span',itemprop='streetAddress').string

        #built_up
        grabbed['built_up'] = soupp[2].find('div',itemprop='value').text

        #land area
        grabbed['land_area'] = soupp[4].find('div',itemprop='value').text

        #bedrooms
        grabbed['bedrooms'] = soup.find('span',itemprop='numberOfRooms').text

        #bathrooms
        grabbed['bathrooms'] = soup.find('div',class_='property-info-element baths').text.strip()

        #monthly installment
        grabbed['monthly_installment'] = getMonthlyInstallment(int(tempprice))

        #land title
        grabbed['land_title'] = soup.find('div',class_='list-group-item-heading').text.strip()

        #tenure
        grabbed['tenure'] = soupp[10].find('div',itemprop='value').text

        #price_per_Sqft 
        grabbed['price_per_sqft'] = soupp[5].find('div',itemprop='value').text

        #furnishing
        grabbed['furnishing'] = soupp[6].find('div',itemprop='value').text
        
        print(grabbed)

        data['list'].append(grabbed)
        i+=1
    
    print(data)
    # dat = json.dumps(data)
    # sendToDB(dat)
    print(len(data['list']))
    return data

def getMonthlyInstallment(price):
    time.sleep(30)
    res = requests.get(constants.monthrepayapi+str(price),headers = constants.header , proxies = constants.proxies)
    parsed = res.json()
    done = parsed[0]["monthlyRepayment"]
    return done


#this sendToDB function is not working for now
def sendToDB(data):
    app = Flask(__name__)
    app.secret_key= 'secret'
    app.config['MYSQL_DATABASE_USER'] = YOUR_DBUSER
    app.config['MYSQL_DATABASE_PASSWORD'] = YOUR_DBPASS
    app.config['MYSQL_DATABASE_DB'] = YOUR_DBNAME
    app.config['MYSQL_DATABASE_HOST'] = YOUR_DBHOST

    #init MySQL
    # mysql = MySQL(app)
    # mysql.init_app(app)
    # print(mysql)
    # if __name__ == '__main__':
    #     app.run()
    mysql = MySQL(app)
    mysql.init_app(app)
    conn = mysql.connect()
    cur = conn.cursor()

    i = 0
    print(len(data["list"]))
    a = int(len(data['list']))

    while i < a : 
        
        #cur = conn.cursor()
        cur.execute("INSERT INTO scraped (links, name, type,price, address, built_up,land_area, bedrooms,bathrooms, monthly_installment , land_title, tenure, price_per_sqft, maintenance_fee , furnishing , state ) VALUES ( %s,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",  (data["list"][i]["link"],data["list"][i]["name"],data["list"][i]["type"],data["list"][i]["price"],data["list"][i]["address"],data["list"][i]["built_up"],data["list"][i]["land_area"],data["list"][i]["bedrooms"],data["list"][i]["bathrooms"],data["list"][i]["monthly_installment"],data["list"][i]["land_title"],data["list"][i]["tenure"],data["list"][i]["price_per_sqft"],data["list"][i]["maintenance_fee"],data["list"][i]["furnishing"],data["list"][i]["state"]))
        conn.commit()
        # cur.close()
        i+=1

    return "done"


