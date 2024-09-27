
# print("Текущая директория:",    os.getcwd())
# if os.path.exists("test"): #если путь содержит директорию"test"
#     os.chdir("test")      #изменять существуюшую директорию на "test"
# else:
#     os.mkdir('test')     #создание папки в текущей директории
#     os.chdir("test")
# print("Текущая директория:", os.getcwd())
# # os.makedirs(r'test1\test2')    #создание вложенных папок
#
# print(os.listdir())     #файлы и папки внутри рабочей директории(без вложенных)
# for i in os.walk("."):
#     print(i)
# os.chdir(r'C:\Users\petro\PycharmProjects\pythonProject2')  #меняет текущую директорию
# print("Текущая директория:", os.getcwd())
# print(os.listdir())
# file=[f for f in os.listdir() if os.path.isfile(f)]      #список файлов
# dirs=[d for d in os.listdir() if os.path.isdir(d)]       #список директорий
# print(file)                                              #печать файлов
# print(dirs)                                              #печать директорий
# os.startfile(file[22])                                   #запуск файла
# print(os.stat(file[22]))                                 #инфо о файле
# print(os.stat(file[22]).st_size)                         #инфо о размере 22го файла в списке
# os.system("pip install random2")

import os
from datetime import datetime

os.chdir('.')

directory="."
# abs_path=os.path.abspath("test_file.txt")
# print("абсолютный путь: ", abs_path)
for root,dirs,files in os.walk(directory):
    for file in files:
        filepath=os.path.join(root,file)
        #получили относительный путь к файлу)
        filetime=datetime.fromtimestamp(os.path.getmtime(filepath))
        # filetime=datetime.fromtimestamp(filetime_0)
        # print(filetime)
        filesize=os.path.getsize(filepath)
        # print(filesize)
        parent_dir=os.path.dirname(filepath)
        # print(parent_dir)

        print(f'Обнаружен файл: {file}, путь: {filepath}, Размер: {filesize} байт, \n'
      f'Время изменения: {filetime}, Родительская директория: {parent_dir}')
