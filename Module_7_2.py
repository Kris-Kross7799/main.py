
def custom_write(file_name, strings: list):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions={}
    number=1
    for string in strings:
        string_positions[(number,file.tell())]=string
        file.write(string + '\n')
        number+=1
    # file.close()
    # file = open(file_name, 'r', encoding='utf-8')
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('new.txt', info)
for elem in result.items():
  print(elem)

