# # # list = ['one', 'two', 'three']
# # # list_2 = [1, 3, 6, 5]
# # # sum = 8
# # for i in range(1, 11):
# #     for k in range(1, 11):
# #         print(f'{i}x{k}={i*k}')
# #     # print([k])
# #     # sum += list_2[i]
# #print(sum)
# list=[1,2,3,4,5]
# list_2=['one', 'two', 'three', 'four', 'five']
#
# dict=dict(zip(list, list_2))
# print(dict)
# for i in dict:
#      for i, k in dict.items():
#        print(i, k)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in (numbers):
    n = i
    k = 0
    for j in range(1, n + 1):
        if i % j == 0:
            k += 1
    if k == 2:
        primes.append(i)

    else:
        not_primes.append(i)
    # break
    print(f'{i}/{j}={i % j}')
print(primes)
print(not_primes)
