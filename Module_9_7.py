
def is_prime(func):
    def wrapper(*args,**kwargs):
        num=func(*args,**kwargs)
        for i in range(2, num):
            if num<2 or num % i == 0:
                print("Составное")
                break
        else:
            print("Простое")
        return num
    return wrapper


@is_prime
def sum_three(x,y,z):
    return x+y+z

result = sum_three(2, 3, 7)
print(result)



# def is_prime(func):
#     def wrapper(*args,**kwargs):
#         num=func(*args,**kwargs)
#         if num < 2:
#             return "Составное"
#         else:
#             for i in range(2, num-1):
#                 if num % i == 0:
#                     return "Составное"
#                     break
#             else:
#                 return "Простое"
#         return num
#     return wrapper
#



