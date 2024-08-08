def get_matrix(n, m, Value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(Value)
    return(matrix)


rez_1 = get_matrix(2, 2, 10)
rez_2 = get_matrix(3, 5, 42)
rez_3 = get_matrix(3, 5, 11)
print(rez_1)
print(rez_2)
print(rez_3)
