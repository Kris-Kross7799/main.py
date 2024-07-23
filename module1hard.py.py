students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students=sorted(students)
print("Ученики по алфавиту:", sorted_students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
avg=sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])
avg_1=list(avg)
print("Средние баллы:", avg_1)
Total=dict(zip(sorted_students, avg_1))
print("Вуаля!-", Total)





