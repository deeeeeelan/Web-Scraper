from flask import Flask,jsonify
app = Flask(__name__)
import constants 
import requests
import functions
import json

@app.route("/", methods =['POST'])
def postmethod():
    link = functions.getLinks()
    data = functions.getData(link)
    res = json.dumps(data)
    return res

@app.route("/", methods =['GET'])
def getmethod():
    return "Please use POST method instead"

if __name__ == '__main__':
    app.run()
