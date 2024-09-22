# print('Привет'+" Питон"+str(14))
# print("Меня зовут %(name)s, мне %(age)s лет" %{'name':"Кристина", 'age':'34'})
# print('Я учусь в {} - {}, {}-{}'.format('Урбан', 'University', 'я', "студент"))
# print('Я учусь в {0} - {1}, {2}-{3}. {0}-{1}'.format('Урбан', 'University', 'я', "студент"))
# print('Я учусь в {title} - {postfix}'.format(title='Урбан', postfix='Университет'))


team1='Мастера кода'
team2='Волшебники данных'
team1_num=5                    #количество участников первой команды
team2_num=6                    #количество участников второй команды
score_1=40                     #количество задач, решённых командой 1
score_2=42                     #количество задач, решённых командой 2
team1_time=18015.2
team1_time=1552.512
team2_time=10717.6
team2_time=2153.31451
tasks_total=score_1+score_2
time_avg=round((team1_time+team2_time)/(score_1+score_2),1)

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = (f"Победа команды {team1}")
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = (f"Победа команды {team2}")
else:
    challenge_result = (f"Ничья")

#использование %:
print('В команде %s участников: %s' %(team1, team1_num))
print('Итого, сегодня в командах участников:  %s' %(team1_num+team2_num))

#format():
print('Команда {} решила задач: {}'.format(team2, score_2))
print("{} решили задачи за {} c!".format(team2, round(team2_time,1)))

#использование f-строк:
print(f'Команды решили {score_1} и {score_2} задачи')
print(f"Результаты битвы: {challenge_result}!")
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} с на задачу')





