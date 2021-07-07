"""
-Merge sort is a divide and sort algorithm
-Divide the input arrays into two halves and we keep halving recursively until they
become too small that they cannot be broken further
-Merge halves by sorting them
"""

def mergeSort(customList, l, m, r):
    n1 = m - l +1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        l[i] = customList[l + i]

    for i in range(n2):
        R[i] = customList[m + 1 + i]