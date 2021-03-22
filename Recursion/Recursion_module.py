def Recursion(n):
    if n<1:
        print("{} is less than 1." .format(n))

    else:
        Recursion(n-1)
        print(n)


Recursion(4)