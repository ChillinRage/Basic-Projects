# some keys
ascending  = lambda x, y: x <= y
descending = lambda x, y: x >= y

'''
in-place sort: no return (void)
default (binary) key for comparison: ascending
'''
def MergeSort(arr, key = ascending, left = 0, right = None):
    if (right == None): # initialised value
        right = len(arr) - 1;
    if ((left == right) or (not arr)): # only 1 element or empty array
        return

    mid = left + (right - left)//2
    MergeSort(arr, key, left, mid)     # sort left half
    MergeSort(arr, key, mid + 1, right) # sort right half

    # merge 2 sorted portions
    
    temp = mid + 1
    
    while ((left <= mid) and (temp <= right)):
        if ( key(arr[left], arr[temp]) ): # left is in place
            left += 1
        else:
            # shift every element between left and temp back 1
            # insert the temp element at left
            # update all pointer
            shift(arr, left, temp)
            left += 1
            temp += 1
            mid  += 1 # end of left-half shifted back by 1


# shift all elements between start and end-1 back by 1
# insert element at end to start
def shift(arr, start, end):
    temp  = arr[end] # element to be inserted at start
    index = end

    for i in range(end, start, -1):
        arr[i] = arr[i - 1]

    arr[start] = temp



def test():
    arr1 = [9,8,7,6,5,4,3,2,1]
    arr2 = [8,7,6,5,4,3,2,1]
    arr3 = [5,3,2,9,1,6,3,7,4]
    arr4 = []
    arr5 = [1,1,1,1,1,1]
    MergeSort(arr1, ascending)
    MergeSort(arr2, descending)
    MergeSort(arr3)
    MergeSort(arr4)
    MergeSort(arr5)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)
    print(arr5)
