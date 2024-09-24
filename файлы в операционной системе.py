import os
from datetime import datetime

directory='.'
# abs_path=os.path.abspath("test_file.txt")
# print("абсолютный путь: ", abs_path)
for root,dirs,files in os.walk(directory):
    for file in files:
        file="test_file.txt"
        root=os.path.dirname(os.path.abspath(file))
        filepath=os.path.join(root,file)
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

