from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import sqlite3
import re
import os
import time
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)

class Articles(Resource):
    def get(self):
        con = sqlite3.connect('sports_plus.db')
        df = pd.read_sql_query('SELECT * from homepage', con)
        df = df.to_dict(orient='index')
        return {'data': df}, 200

api.add_resource(Articles, '/articles')

if __name__ == '__main__':
    app.run()