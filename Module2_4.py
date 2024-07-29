numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in (numbers):
    if i > 1:
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
        #print(f'{i}/{j}={i % j}')
print("начальный список: ", numbers)
print("список простых чисел: ", primes)
print("список непростых чисел: ", not_primes)
