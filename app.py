from flask import Flask,jsonify
app = Flask(__name__)
import constants 
import requests
import functions
import json

@app.route("/run", methods =['POST'])
def postmethod():
    link = functions.getLinks()
    data = functions.getData(link)
    res = json.dumps(data)
    return res

@app.route("/run", methods =['GET'])
def getmethodx():
    return "Please use POST method instead"

if __name__ == '__main__':
    app.run()

@app.route("/", methods =['GET','POST'])
def getmethod():
    return "Please use /run on POST method"

if __name__ == '__main__':
    app.run()
