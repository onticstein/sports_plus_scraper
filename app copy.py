from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import sqlite3
import re
import os
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)

class Articles(Resource):
    def get(self):
        # Delete Old Data
        os.remove('sports_plus.db')

        # Open URL and Establish BS4
        url = 'https://www.usatodaysportsplus.com/'
        html = request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Establish DB Connection
        con = sqlite3.connect('sports_plus.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS homepage
                        (title, image_url, category, date_time)''')

        # Define Lists
        title = []
        image_url = []
        category = []
        date_time = []
        list_of_list = [title, image_url, category, date_time]

        # Breaking Story Section
        bs_section = soup.find('a', {'class': 'gnt_m_he gnt_m_he_a'})

        try:
            bs_title = bs_section.text.strip()
            title.append(bs_title)
        except:
            title.append(' ')

        try:
            bs_image = bs_section.img['src'].strip()
            image_url.append(bs_image)
        except:
            image_url.append(' ')

        try:
            bs_category = bs_section.div['data-c-ms'].strip()
            category.append(bs_category)
        except:
            category.append(' ')

        try:
            bs_date_time = bs_section.div['data-c-dt'].strip()
            date_time.append(bs_date_time)
        except:
            date_time.append(' ')

        # Triplet Section Beneath Breaking Story
        t_section = soup.find_all('a', {'class': 'gnt_m_tl'})

        for box in t_section:

            box_divs = box.find_all('div')

            try:
                t_title = box.text.strip()
                title.append(t_title)
            except:
                title.append(' ')

            try:
                t_image = box.img['src'].strip()
                image_url.append(t_image)
            except:
                image_url.append(' ')

            try:
                t_category = box_divs[1]['data-c-ms']
                category.append(t_category)
            except:
                category.append(' ')

            try:
                t_date_time = box_divs[1]['data-c-dt']
                date_time.append(t_date_time)
            except:
                date_time.append(' ')

        # More Stories Section
        ms_section = soup.find_all('a', {'class': 'gnt_m_sl_a'})

        for box in ms_section:

            try:
                ms_title = box.text.strip()
                title.append(ms_title)
            except:
                title.append(' ')

            try:
                ms_image = box.img['data-gl-srcset']
                image_url.append(ms_image)
            except:
                image_url.append(' ')

            try:
                ms_category = box.div['data-c-ms']
                category.append(ms_category)
            except:
                category.append(' ')

            try:
                ms_date_time = ' '
                date_time.append(ms_date_time)
            except:
                date_time.append(ms_date_time)

        # Additional Stories Section
        regex = re.compile('.*gnt_m_lb_a gnt_m_lb_a__i.*')

        as_section = soup.find_all('a', {'class': regex})

        for box in as_section:
            
            try:
                as_title = box.text.strip()
                title.append(as_title)
            except:
                title.append(' ')

            try:
                as_image = box.img['data-gl-srcset']
                image_url.append(as_image)
            except:
                image_url.append(' ')

            try:
                as_category = box.div['data-c-ms']
                category.append(as_category)
            except:
                category.append(' ')

            try:
                as_date_time = box.div['data-c-dt']
                date_time.append(as_date_time)
            except:
                date_time.append(' ')

        temp_list = []
        x = 0

        while x < len(date_time):
                temp_list.append(title[x])
                temp_list.append(image_url[x])
                temp_list.append(category[x])
                temp_list.append(date_time[x])
                cur.execute("INSERT INTO homepage VALUES (?, ?, ?, ?)", temp_list)
                temp_list.clear()
                x += 1
        con.commit()

        df = pd.read_sql_query('SELECT * from homepage', con)
        df = df.to_dict(orient='index')
        return {'df': df}, 200

api.add_resource(Articles, '/articles')

if __name__ == '__main__':
    app.run()