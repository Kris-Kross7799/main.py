import os
from datetime import datetime


directory='.'
for root,dirs,files in os.walk(directory):
    for file in files:
        file="test_file.txt"
        path1=directory
        # print("путь1: ", path1)
        path2=file
        # print("путь2: ", path2)
        filepath=os.path.join(path1,path2)
        # print("Полный путь к файлу: ", filepath)
        filetime=datetime.fromtimestamp(os.path.getmtime(file))
        # filetime=datetime.fromtimestamp(filetime_0)
        # print(filetime)
        filesize=os.path.getsize(file)
        # print(filesize)
        parent_dir=os.path.dirname(filepath)
        # print(parent_dir)

print(f'Обнаружен файл: {file}, путь: {filepath}, Размер: {filesize} байт, \n'
      f'Время изменения: {filetime}, Родительская директория: {parent_dir}')

