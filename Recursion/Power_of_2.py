def PowerRecursion(n):
    if n==0:
        return 1
    else:
        power = PowerRecursion(n-1)
        return power*2


print(PowerRecursion(5))
"""
Infinite Recursion can lead to system crash
 In iterative Soltuions, Infinite iterations can lead to infinite CPU Cycles

Recursive algorithms are space inefficient (uses atleast O(N))

Recursion is useful when we traverse through a TREE

Time and Space Complexity is very high when we use recursion
"""