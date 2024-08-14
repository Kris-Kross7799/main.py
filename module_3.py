# # a=6
# # b=12
# # print(a, b)
# # def printer():
# #     c=10
# #     d=15
# #     global a,b
# #     a='str'
# #     b='str_2'
# #     print('local', c,d)

calls = 0


def string_info(string):
    global calls
    length = len(string)
    big = string.upper()
    small = string.lower()
    t = (length, big, small)
    calls += 1
    return t


def is_contains(string, list_to_search):
    global calls
    calls += 1
    string_2 = string.lower()
    c = 0
    for i in range(len(list_to_search)):
        a = list_to_search[i]
        a = a.lower()
        if string_2 in a:
            c += 1
    if c >= 1:
        return True
    else:
        return False
    print(b)


print(string_info('capyBARA'))
print(string_info('ChuPaCaBRa'))
print(is_contains('more', ['a', 'moreMa', 'Moe', 'mArE']))
print(is_contains('mARe', ['a', 'moreMa', 'Moe', 'mArE']))


print(calls)
