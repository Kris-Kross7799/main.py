
#REQUESTS
print('REQUESTS:')
import requests
result=requests.get('https://yandex.ru')
print(result.content) #печать содержимого в байтовом виде
print(result.text) #печать содержимого в строковом виде
print(result.headers) #печать заголовков

query = {'q': 'Ladybug', 'order': 'moovie', 'min_width': '1000', 'min_height': '800'}  # условие поиска
req = requests.get('https://yandex.ru', params=query)  # передача параметров для поиска
print(req.url)  # печать найденного
print('-' * 37)

# PANDAS:
print('PANDAS:')
import pandas as pd

school= {'фамилия':['Алёшина', 'Петрова', 'Кузнецов', 'Запашный'], "год рождения": ["2017", "2015", "2017", "2016"], "увлечения": ["рисование", "волейбол", "валяние", "теннис"]}
table=pd.DataFrame(school)
print(table)
print('-' * 37)

#импорт файла CSV для анализа данных:
print('Импорт данных из файла Internet Speed 2022:')
df=pd.read_csv('Internet Speed 2022.csv')
print(df)
print("\nБез пропусков:")
df=df.dropna()
print(df)
print('Количество строк уменьшилось на 41')
print("\nСортировка по возрастанию по столбцу mobile:")
print(df.sort_values('mobile', ascending=True))
print("\nСортировка по убыванию по столбцу mobile:")
print(df.sort_values('mobile', ascending=False))

print('Оценка данных:')
print(df.describe())
print('mean-средняя скорость, \nstd-стандартное отклонение, \nmin-минимальное значение, \nmax-максимальное значение, \n25%,50%,75%-процентили')
print('\nСтраны со скоростью мобильного интнрнета <100 мБит/с:')
print(df[df['mobile']<100])

print('-' * 37)
#MATPLOTLIB
print('MATPLOTLIB:')
print('График:')
from matplotlib import pyplot as plt
x=[1,3,5,5.5,6,7,8]
y=[25,36,24,25,35,76,25]
plt.plot(x,y,color='green', marker="o", markersize=3) #Построим график
plt.title('График') #Подпишем график
plt.xlabel('Ось Х') #Подпишем ось Х
plt.ylabel('Ось Y') #одпишем ось Y
plt.show()          #Создадим визуализацию

print('Диаграмма:')
# x=list(df['country'])
# y=list(df['mobile'])
x=['Япония', 'Монако', 'Израиль', 'Корея', 'Финляндия']
y=[258.2,456,258,159,357.5]
plt.bar(x,y, color='pink', label='Скорость мобильного интернета в разных странах') #Строим диаграмму
plt.plot(x, y, color='blue')   #Строим график с теми же данными
plt.title('Диаграмма')
plt.xlabel('Страна')
plt.ylabel('Скорость моб.интернета, кБит/с')
# plt.legend(x,y)
plt.show()

print('Круговая диаграмма:')
plt.pie(y, labels=x) #Строим круговую диаграмму
plt.title('Соотношение скорости интернета в разных странах')
plt.show()



