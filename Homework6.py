my_dict = {'Mark': 2001, 'Teodor': 2012, 'Kantemir': 1999}
print(my_dict)
print("значение существующего:", my_dict['Mark'])
print("значение несуществующего:", my_dict.get('Anna'))
my_dict.update({'Kris': 1981,
                'Anna': 1984})
print("значение изъятого элемента:", my_dict.pop('Mark'))
print("список без изъятого элемента:", my_dict)

my_set = {12,13,14,15,15,17,18,20,19,16,15}
print("множество:", my_set)
my_set.add(1)
my_set.add(2)
my_set.discard(16)
print("обновленное множество:", my_set)

