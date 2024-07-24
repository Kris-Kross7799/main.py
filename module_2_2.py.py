
First=int(input ("Введите число:"))
Second=int(input ("Введите число:"))
Third=int(input ("Введите число:"))
if First==Second and Second ==Third:
    print(3)
elif First==Second:
    print(2)
elif First==Third:
    print(2)
elif Second==Third:
    print(2)
elif First!=Second or First!=Third or Second!=Third:
    print(0)

