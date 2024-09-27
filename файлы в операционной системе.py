

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
