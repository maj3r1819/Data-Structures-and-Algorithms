def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]

    print(customList)


clist = [5,4,3,2,1]
bubbleSort(clist)
ba =  [5,1, 2, 5, 6, 8, 9,10]
"""
When to use Bubble Sort?
-Space is a concern
-Easy to Implement

WHen to avoid?
-time complexity is very high O(n^2). so cannot use where time is an issue
"""
