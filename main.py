# Import Libraries
import sqlite3
from urllib import request
from bs4 import BeautifulSoup

# Open URL and Establish BS4
url = 'https://www.usatodaysportsplus.com/'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Establish DB Connection
con = sqlite3.connect('sports_plus.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS homepage
                (title PRIMARY KEY, image_url, category, date_time)''')

# Define Lists
title = []
image_url = []
category = []
date_time = []
list_of_list = [title, image_url, category, date_time]

# Main Title
main_title = soup.find_all("a", {"class": "gnt_m_he gnt_m_he_a"})
for item in main_title:
    print(item.text)
    title.append(item.text)

# Main Title Image
main_img = soup.find_all("img", {"class": "gnt_m_he_i"})
for item in main_img:
    print(item['src'])
    image_url.append(item['src'])

# Main Title Category
main_category = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts gnt_sbt__mg gnt_lbl_pm"})
if not main_category:
    try:
        main_category2 = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts gnt_sbt__mg"})
        for item in main_category2:
            print(item['data-c-ms'])
            category.append(item['data-c-ms'])
    except:
        category.append(' ')
for item in main_category:
    print(item['data-c-ms'])
    category.append(item['data-c-ms'])

# Main Title Date Time
main_datetime = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts gnt_sbt__mg"})
if not main_datetime:
    try:
        main_datetime2 = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts gnt_sbt__mg"})
        for item in main_datetime2:
            print(item['data-c-dt'])
            date_time.append(item['data-c-dt'])
    except:
        date_time.append(' ')
for item in main_datetime:
    print(item['data-c-dt'])
    date_time.append(item['data-c-dt'])

# Triplet Titles
trip_titles = soup.find_all("div", {"class": "gnt_m_tl_c"})
for item in trip_titles:
    print(item.text)
    title.append(item.text)

# Triplet Images
trip_imgs = soup.find_all("img", {"class": "gnt_m_tl_i"})
for item in trip_imgs:
    print(item['src'])
    image_url.append(item['src'])

# Triplet Categories Part 1
trip_category = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms"})
x = 0
while x < 1:
    current_item = trip_category[x]
    print(current_item['data-c-ms'])
    category.append(current_item['data-c-ms'])
    x += 1

# Triplet Categories Part 2
trip_category = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
for item in trip_category:
    print(item['data-c-ms'])
    category.append(item['data-c-ms'])

# Triplet Categories Part 3
trip_category = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms"})
x = 1
while x < 2:
    current_item = trip_category[x]
    print(current_item['data-c-ms'])
    category.append(current_item['data-c-ms'])
    x += 1

# Triplet Date Time EMPTY
date_time.append(' ')

# Triplet Date Time
trip_datetime = soup.find_all("div", {"class": "gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
for item in trip_datetime:
    print(item['data-c-dt'])
    date_time.append(item['data-c-dt'])

# Triplet Date Time EMPTY
date_time.append(' ')

# More Stories Titles
ms_titles = soup.find_all("a", {"class": "gnt_m_sl_a"})
for item in ms_titles:
    print(item.text)
    title.append(item.text)

# More Stories Images
ms_imgs = soup.find_all("img", {"class": "gnt_m_sl_i"})
for item in ms_imgs:
    print(item['data-gl-src'])
    image_url.append(item['data-gl-src'])

# More Stories Categories
ms_category = soup.find_all("div", {"class": "gnt_m_sl_a_sb"})
for item in ms_category:
    print(item['data-c-ms'])
    category.append(item['data-c-ms'])

# More Stories Date Time
x = 0
while x < 6:
    date_time.append(' ')
    x += 1

# Additional Stories Titles
as_title = soup.find_all("a", {"class": "gnt_m_lb_a"})
for item in as_title:
    print(item.text)
    title.append(item.text)

# Additional Stories Images
as_imgs = soup.find_all("img", {"class": "gnt_m_lb_i"})
for item in as_imgs:
    print(item['data-gl-src'])
    image_url.append(item['data-gl-src'])

# Addition Stories Category Part 1
as_category = soup.find_all("div", {"class": "gnt_m_lb_sbt gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
x = 0
while x < 10:
    current_item = as_category[x]
    print(current_item['data-c-ms'])
    category.append(current_item['data-c-ms'])
    x += 1

# Addition Stories Category EXCLUSIVE
as_category = soup.find_all("div", {"class": "gnt_m_lb_sbt gnt_sbt gnt_sbt__ms"})
for item in as_category:
    print(item['data-c-ms'])
    category.append(item['data-c-ms'])

# Addition Stories Category Part 2
as_category = soup.find_all("div", {"class": "gnt_m_lb_sbt gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
x = 10
while x < 20:
    current_item = as_category[x]
    print(current_item['data-c-ms'])
    category.append(current_item['data-c-ms'])
    x += 1

# Addition Stories Date Time Part 1
as_datetime = soup.find_all("div", {"class": "gnt_m_lb_sbt gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
x = 0
while x < 10:
    current_item = as_datetime[x]
    print(current_item['data-c-dt'])
    date_time.append(current_item['data-c-dt'])
    x += 1

# Addition Stories Date Time EXCLUSE
date_time.append(' ')

# Addition Stories Date Time Part 2
as_datetime = soup.find_all("div", {"class": "gnt_m_lb_sbt gnt_sbt gnt_sbt__ms gnt_sbt__ts"})
x = 10
while x < 20:
    current_item = as_datetime[x]
    print(current_item['data-c-dt'])
    date_time.append(current_item['data-c-dt'])
    x += 1

# DB Data Entry
def data_entry(main_list):
    temp_list = []
    x = 0
    while x < len(category): #len(title) - 1:
            temp_list.append(title[x])
            temp_list.append(image_url[x])
            temp_list.append(category[x])
            temp_list.append(date_time[x])
            cur.execute("INSERT OR IGNORE INTO homepage VALUES (?, ?, ?, ?)", temp_list)
            temp_list.clear()
            x += 1
    con.commit()

data_entry(list_of_list)