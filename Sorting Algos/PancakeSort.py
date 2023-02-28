# ===== some keys =====
ascending  = lambda x,y  : x <= y
descending = lambda x,y : x >= y

def PancakeSort(arr, key = ascending):
    
    for i in range(len(arr) - 1, 0, -1):
        max_index = FindBestIndex(arr, i, key)
        flip(arr, max_index) # flip "max" element to the top
        flip(arr, i)         # flip "max" to ith bottom


# return "maximum" element in the subarray [0, index]
def FindBestIndex(arr, index, key):
    max_index = index
    for i in range(index + 1):
        if (not key(arr[i], arr[max_index])):
            max_index = i

    return max_index

# do a pancake flip from index
def flip(arr, index):
    left = 0
    while (left < index):
        arr[left], arr[index] = arr[index], arr[left]
        left  += 1
        index -= 1

def test():
    arr1 = [9,8,7,6,5,4,3,2,1]
    arr2 = [8,7,6,5,4,3,2,1]
    arr3 = [5,3,2,9,1,6,3,7,4]
    arr4 = []
    arr5 = [1,1,1,1,1,1]
    PancakeSort(arr1, ascending)
    PancakeSort(arr2, descending)
    PancakeSort(arr3)
    PancakeSort(arr4)
    PancakeSort(arr5)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)
    print(arr5)
