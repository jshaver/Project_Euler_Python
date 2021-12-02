from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from Problems import *
from Tools import *

app = Flask(__name__)
api = Api(app)


class Problems_Api(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', required=True, type=int)
        args = parser.parse_args()
        result = solve_001(args['limit'])
        return { 'data': result }, 200

class Tools_Api(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('n', required=True, type=int)
        args = parser.parse_args()
        result = getNthPrimeNumber(args['n'])
        return { 'data': result }, 200
    


api.add_resource(Problems_Api, '/problems')
api.add_resource(Tools_Api, '/tools')


if __name__ == '__main__':
    app.run()