def calculate_structure_sum(*data_structure):
    a = 0
    for i in range(len(data_structure)):
        if isinstance(data_structure[i], dict):
            for key, value in data_structure[i].items():
                a += calculate_structure_sum(key)
                a += calculate_structure_sum(value)
                # print(key)
                # print(value)
        elif isinstance(data_structure[i], list | tuple | set):
            for i in data_structure[i]:
                a += calculate_structure_sum(i)
        elif isinstance(*data_structure, str):
            a += len(*data_structure)
        elif isinstance(*data_structure, int | float):
            a += data_structure[i]
        return a


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
