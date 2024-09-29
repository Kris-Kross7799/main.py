def personal_sum(numbers):
    try:
        result=0
        incorrect_data=0
        for i in numbers:
            try:
                result+=i
            except TypeError:
                incorrect_data+=1
                print(f"Некорректный тип данных: {i}")
        return (result, incorrect_data)
    except TypeError as exc:
        print("Некорректный тип данных")
def calculate_average(numbers):
    try:
        numbers=list(numbers)
        num_count=0
        for i in numbers:
            if isinstance(i,int) or isinstance(i, float):
                num_count+=1
        sum=personal_sum(numbers)
        srednee=sum[0]/num_count
        return srednee
    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print("В numbers записан некорректный тип данных")


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

