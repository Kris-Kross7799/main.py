import random
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER)
''')


# for i in range(4):
#     cursor.execute("INSERT INTO Products (title,description, price) VALUES(?,?,?)",(f"Продукт_{i+1}", f"Описание_{i+1}", f"{(i+1)*100}"))
# cursor.execute("DELETE FROM Products")

def get_all_products():
    cursor.execute('SELECT id, title,description,price FROM Products')
    products=cursor.fetchall()
    return products

connection.commit()
# connection.close()