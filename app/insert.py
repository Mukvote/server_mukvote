import pymysql
import pandas as pd

import sys
import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(find_dotenv())

mydb = pymysql.connect(host=os.getenv("DB_SERVICE"),
    user=os.getenv('DB_USER'),
    passwd=os.getenv("DB_PASS"),
    db=os.getenv('DB_NAME'))

cursor = mydb.cursor()


sql = 'INSERT INTO restaurant (restaurant_id, restaurant_name, restaurant_place, restaurant_category, restaurant_priority, order_count ) VALUES(%s, %s, %s, %s, %s, %s)'
csv_input = pd.read_csv("DB_DATA.csv", nrows = 106, dtype={"restaurant_id" : int, "restaurant_name" : str, "restaurant_place" : str, "restaurant_category" :str, "restaurant_priority" : int, "order_count" : int}, encoding = "utf8")
csv_input = csv_input.values
print(csv_input)
for row in csv_input:
    cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], int(row[4]), int(row[5])))


mydb.commit()
cursor.close()
print("Done")
