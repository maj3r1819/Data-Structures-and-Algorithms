def GCD(x,y):
    x = max(x,y)
    y = min(x,y)
    if x%y == 0:
        return y
    return GCD(y,x%y)


print(GCD(48,18))
print(GCD(100,75))


'''
Algorithm:
GCD(48,18)
Step 1: 48/18 = 2 and remainder = 12
Step 2: 18/12 = 1 and remainder = 6
***Step 3: 12/6 = 2 and remainder = 0***

'''
