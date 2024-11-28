import random
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users1(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

# Заполняем 10 записями:
# for i in range(10):
#     cursor.execute("INSERT INTO Users1 (username, email,age, balance) VALUES(?,?,?,?)",(f"user_{i+1}", f"example_{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(10):
#     cursor.execute("UPDATE Users1 SET balance=? WHERE id%2!=0", (500,))

# Удаление строк:
count = 1
while count <= 10:
    cursor.execute("DELETE FROM Users1 WHERE id=?", (count,))
    count += 3

#Выборка всех записей при помощи fetchall(), где возраст не равен 60:
cursor.execute("SELECT username,email, age, balance FROM Users1 WHERE age !=60")
users=cursor.fetchall()
for i in users:
    print(i)

#Удаление записи с ID=6:
cursor.execute("DELETE FROM Users1 WHERE id=6")

#Общее кол-во записей:
cursor.execute('SELECT COUNT(*) FROM Users1')
counter=cursor.fetchone()[0]
print("Количество записей:", counter)

#Сумма балансов:
cursor.execute('SELECT SUM(balance) FROM Users1')
summ=cursor.fetchone()[0]
print("Сумма записей:", summ)

#Среднее значение:
print(f"Среднее значение по столбцу Баланс: {summ / counter}")





connection.commit()
connection.close()
