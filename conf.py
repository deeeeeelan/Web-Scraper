from flask import Flask,jsonify
app = Flask(__name__)
import constants 
import requests
import functions
import json

@app.route("/", methods =['POST'])
def postmethod():
    return "Test"
# app.run()

@app.route("/", methods =['GET'])
def getmethod():
    link = functions.getLinks()
    data = functions.getData(link)
    res = json.dumps(data)

    #constants.zzz
    #aaa = requests.get(constants.monthrepayapi+'1000000', headers = constants.header, proxies = constants.proxies)
    # bbb = str(aaa)
    # print(bbb)
    # linkk = str(link)
    return res
# app.run()

