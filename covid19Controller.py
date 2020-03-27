# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

from urllib.request import urlopen, Request
import json
import pandas as pd
from pandas.io.json import json_normalize


app = Flask(__name__)
api = Api(app)

class AgeCalculator(Resource):
    
    def ageCalculate(self,ageList,startAge,endAge,ageType):
        count = 0
        for items in ageList.iteritems():
            index, age = items
            if(age!=""):
                ageInt = int(age)
                if(ageType==0):
                    if(ageInt>=startAge):
                        count = count + 1
                elif(ageType==1):
                    if(ageInt<=endAge):
                        count = count + 1
                elif(ageType==2):
                    if(ageInt>=startAge and ageInt<=endAge):
                        count = count + 1
                    
        return count
        
                    
    
    def get(self):
        startAge =  request.args.get('startAge')
        endAge = request.args.get('endAge')
        if(startAge!="" and endAge!=""):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            reg_url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org"
            req = Request(url=reg_url, headers=headers)
            html = urlopen(req).read()
            patientsJson = json.loads(html)
            patientsDataFrame = json_normalize(patientsJson["data"]["rawPatientData"])
            ageCount = self.ageCalculate(patientsDataFrame['ageEstimate'],int(startAge), int(endAge), 2)
            return {'ageCount':ageCount}
        
        elif(startAge==""):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            reg_url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org"
            req = Request(url=reg_url, headers=headers)
            html = urlopen(req).read()
            patientsJson = json.loads(html)
            patientsDataFrame = json_normalize(patientsJson["data"]["rawPatientData"])
            ageCount = self.ageCalculate(patientsDataFrame['ageEstimate'],0, int(endAge), 1)
            return {'ageCount':ageCount}
        
        elif(endAge==""):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            reg_url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org"
            req = Request(url=reg_url, headers=headers)
            html = urlopen(req).read()
            patientsJson = json.loads(html)
            patientsDataFrame = json_normalize(patientsJson["data"]["rawPatientData"])
            ageCount = self.ageCalculate(patientsDataFrame['ageEstimate'],int(startAge), 0, 0)
            return {'ageCount':ageCount}
        
        return {'error':"start age and end age are empty"}

api.add_resource(AgeCalculator, '/calculateAge')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(debug=True)
