# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class AnswerQuery(Resource):
    def get(self):
        question = request.args.get('q')
        return {'hello': question}

api.add_resource(AnswerQuery, '/Search')


class BuildandTrain(Resource):
    def post(self):
        req_data = request.get_json()
        print(req_data)

api.add_resource(BuildandTrain, '/BuildandTrain')

if __name__ == '__main__':
    app.run(debug=True)
