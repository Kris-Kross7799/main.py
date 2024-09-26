# print("******* Какой хороший день, предлагаю научиться работать "
# "с исключениями! *******")
#
# try:
#     i = int(input("Введите число: "))
#     print(round(10 * (1 / i), 2))
#     print("Готово!")
# except ValueError as exc:
#     print("Нет такой цифры:", exc)
# except ZeroDivisionError as exc:
#     print("На ноль делить нельзя:!", exc)
# else:
#     print("Ура, все правильно написали!")
# finally:
#     print("Завершили урок.")

# try:
#     file=open("new.txt")
# except OSError as exc:
#     print(f'Что-то не так:, {exc},{exc.args}')
# else:
#     print(f"Вот, пожалуйте: \n{file.readline}")

def add_everything_up(a, b):
    try:
        sum=(round(a+b, 3))
    except TypeError as exc:
        a=str(a)
        b=str(b)
        sum=a+b
    finally:
        return(sum)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
