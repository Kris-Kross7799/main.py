calls = 0


def count_calls(f):
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls(1)
    length = len(string)
    big = string.upper()
    small = string.lower()
    t = (length, big, small)
    return t


def is_contains(string, list_to_search):
    count_calls(1)
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


print(string_info('capyBARA'))
print(string_info('ChuPaCaBRa'))
print(string_info('ChuPa'))
print(is_contains('more', ['a', 'moreMa', 'Moe', 'mArE']))
print(is_contains('mARe', ['a', 'moreMa', 'Moe', 'mArE']))

print(calls)
