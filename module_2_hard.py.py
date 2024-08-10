# #
# # def password(numbers):
# #
# #     for i in range[1, numbers]:
# #         path = []
#
# def password(number):
#     pass_ = ''
#     for i in range(1, number):
#         for j in range(i + 1, number):
#             if number % (i + j) == 0:
#                 pass_ += str(i) + str(j)
#     return pass_
#
# print('Введите число: ')
# x=input()
# print(password(int(x)))

n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

rezult = []

for i in n:
    for j in range(1, i):
        for k in range(j + 1, i):
            if i % (j + k) == 0:
                rezult += j, k


    print(i, rezult)
    rezult=[]
