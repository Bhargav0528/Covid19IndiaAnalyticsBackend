# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class AgeCalculator(Resource):
    def get(self):
        startAge = int(request.args.get('startAge'))
        endAge = int(request.args.get('endAge'))
        return {'startAge': startAge, 'endAge': endAge}

api.add_resource(AgeCalculator, '/calculateAge')


if __name__ == '__main__':
    app.run(debug=True)
