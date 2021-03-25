def binary(num):
    if num == 0:
        return 0
    return num%2 + 10*binary(num//2)

print(binary(13))