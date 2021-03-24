def factorial(num):
    num = int(num)
    try:
        if num in [0,1]:
            return 1
        else:
            return num*factorial(num-1)
    except BaseException:
        print("Do not enter negative number")

print(factorial(4))