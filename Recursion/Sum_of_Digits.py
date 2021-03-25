def sum(num):
    if num%10 == num:
        return num
    return int(num%10) + sum(num//10)


print(sum(123))