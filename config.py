from flask import Flask
from flaskext.mysql import MySQL

#instaniation
app = Flask(__name__)
app.secret_key= 'secret'

#config
app.config['MYSQL_DATABASE_USER'] = 'b86931380feac2'
app.config['MYSQL_DATABASE_PASSWORD'] = 'e5bf2af6'
app.config['MYSQL_DATABASE_DB'] = 'heroku_3ddf690ab05fef8'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-05.cleardb.net'

#init MySQL
mysql = MySQL(app)
mysql.init_app(app)
# print(mysql)
if __name__ == '__main__':
    app.run()