def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 3, 'song')
print_params(16, c=10)
print_params('got')
print_params()
print()
values_list = (1, 'строка', True)
values_dict={'a':7, 'b':False, 'c':'ferz'}

print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = (54.32, 'строка')
print_params(*values_list_2, 42)