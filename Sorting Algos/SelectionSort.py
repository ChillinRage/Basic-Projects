# some keys
ascending  = lambda x, y: x <= y
descending = lambda x, y: x >= y

'''
in-place sort: no return (void)
default (binary) key: ascending
'''
def SelectionSort(arr, key = ascending):

    for i in range(len(arr)):
        index = find_between(arr, i, key)
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp

def find_between(arr, start, key):
    length = len(arr)
    
    if (start >= len(arr)): # invalid start index
        return -1
    
    index = start; # take start element as worst
    worst = arr[start]
    start += 1
    
    while (start < length):
        if (not key(worst, arr[start]) ): # found a worse element
            index = start
            worst = arr[start]

        start += 1

    return index


def test():
    arr1 = [9,8,7,6,5,4,3,2,1]
    arr2 = [8,7,6,5,4,3,2,1]
    arr3 = [5,3,2,9,1,6,3,7,4]
    arr4 = []
    arr5 = [1,1,1,1,1,1]
    arr6 = [1,2,3,4,4,3,2,1]
    SelectionSort(arr1, ascending)
    SelectionSort(arr2, descending)
    SelectionSort(arr3)
    SelectionSort(arr4)
    SelectionSort(arr5)
    SelectionSort(arr6, descending)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)
    print(arr5)
    print(arr6)
test()
