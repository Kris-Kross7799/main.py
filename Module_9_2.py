first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result=[len(i)  for i in first_strings if len(i)>=5]    #в списке длины строк, условие строка не менее 5 симв.
print(first_result)

second_result= [(i,j) for i in first_strings for j in second_strings if len(i)==len(j)] #в кортеже пара слов одинаковой длины из разных списков
print(second_result)

third_string={i:len(i) for i in first_strings+second_strings if len(i)%2==0}  #пара: строка и ее длина из обоих списков, условие-четная длина строки
print(third_string)

