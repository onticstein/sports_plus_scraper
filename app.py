from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import sqlite3
import ast

app = Flask(__name__)
api = Api(app)

class Articles(Resource):
    def get(self):
        con = sqlite3.connect('sports_plus.db')
        df = pd.read_sql_query('SELECT * from homepage', con)
        df = df.to_dict(orient='index')
        return {'df': df}, 200

api.add_resource(Articles, '/articles') # '/articles' is our entry point

if __name__ == '__main__':
    app.run() # run our Flask app

