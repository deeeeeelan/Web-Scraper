from flask import Flask
from flaskext.mysql import MySQL

#instaniation
app = Flask(__name__)
app.secret_key= 'secret'
app.config['MYSQL_DATABASE_USER'] = 'b86931380feac2'
app.config['MYSQL_DATABASE_PASSWORD'] = 'e5bf2af6'
app.config['MYSQL_DATABASE_DB'] = 'heroku_3ddf690ab05fef8'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-05.cleardb.net'

#init MySQL
mysql = MySQL(app)
mysql.init_app(app)
print(mysql)
# if __name__ == '__main__':
#     app.run()
conn = mysql.connect()
cur = conn.cursor()
cur.execute("INSERT INTO scrapex (links, name, type,price, address, built_up,land_area, bedrooms,bathrooms, monthly_installment , land_title, tenure, price_per_sqft, maintenance_fee , furnishing , state ) VALUES ( %s,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",  ("aa","aa","aa",int("200"),"aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa"))
# cur.execute("INSERT INTO scraped (links, name, type,price, address, built_up,land_area, bedrooms,bathrooms, monthly_installment , land_title, tenure, price_per_sqft, maintenance_fee , furnishing , state ) VALUES ( %s,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",  (data["list"][i]["link"],data["list"][i]["name"],data["list"][i]["type"],data["list"][i]["price"],data["list"][i]["address"],data["list"][i]["built_up"],data["list"][i]["land_area"],data["list"][i]["bedrooms"],data["list"][i]["bathrooms"],data["list"][i]["monthly_installment"],data["list"][i]["land_title"],data["list"][i]["tenure"],data["list"][i]["price_per_sqft"],data["list"][i]["maintenance_fee"],data["list"][i]["furnishing"],data["list"][i]["state"])
# data["list"][i]["state"]))

# cur.execute("INSERT INTO scrape (link, name, type,price, address, built_up,land_area, bedrooms,bathrooms, monthly_installment , land_title, tenure, price_per_sqft,furnishing ) VALUES (aa,aa,aa,0,aa,aa,aa,aa,aa,aa,aa,aa,aa,aa,aa,aa")
# data["list"][i]["link"],data["list"][i]["name"],data["list"][i]["type"],data["list"][i]["price"],data["list"][i]["address"],data["list"][i]["built_up"],data["list"][i]["land_area"],data["list"][i]["bedrooms"],data["list"][i]["bathrooms"],data["list"][i]["monthly_installment"],data["list"][i]["land_title"],data["list"][i]["tenure"],data["list"][i]["price_per_sqft"],data["list"][i]["maintenance_fee"],data["list"][i]["furnishing"]),
# data["list"][i]["state"]
conn.commit()
# mysql.commit()