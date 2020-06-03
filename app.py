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
# app.run()

@app.route("/", methods =['GET'])
def getmethod():
    # link = functions.getLinks()
    # data = functions.getData(link)
    # res = json.dumps(data)
    return "Please use POST method instead"
# app.run()

