"""
In Insertion Sort, we take the first element from unsorted array and find its correct position in the sorted array
-repeat
"""

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    print(customList)


clist = [5, 4, 3, 2, 1]
insertionSort(clist)

"""
pros
-space complexity

cons
-time complexity
"""