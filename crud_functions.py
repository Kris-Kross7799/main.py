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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
user_name TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL)
''')

def is_included(user_name):
    check_user = cursor.execute('SELECT * FROM Users WHERE user_name=?', (user_name,))
    connection.commit()
    # connection.close()
    return check_user.fetchone() is not None

def add_user(user_name, email, age, balance=1000):
    cursor.execute(f"INSERT INTO Users (user_name, email, age, balance) VALUES(?,?,?,?)", (user_name, email, age, '1000'))
    connection.commit()
    # connection.close()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


# connection.commit()
# connection.close()


