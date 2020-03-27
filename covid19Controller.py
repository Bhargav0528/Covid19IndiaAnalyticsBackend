# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class AgeCalculator(Resource):
    def get(self):
        startAge =  request.args.get('startAge')
        endAge = request.args.get('endAge')
        return {'startAge': startAge, 'endAge': endAge}

api.add_resource(AgeCalculator, '/calculateAge')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(debug=True)
