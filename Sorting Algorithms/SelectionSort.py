"""
In Selection Sort, we find the minimum element and move it to the sorted
part of the array to make unsorted part sorted.
"""

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index]> customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

clist = [5,4,3,2,1]
selectionSort(clist)