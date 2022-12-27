def reverse_arr(arr):
    #I am aware of arr[::-1], but for the sake of learning, no.
    left  = 0
    right = len(arr) - 1
    
    while left < right:
        #another way to swap elements in array
        arr[left] += arr[right]
        arr[right] = arr[left] - arr[right]
        arr[left] -= arr[right]
            
        left  += 1
        right -= 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def Bubble_sort(arr, reverse = False):
    length = len(arr)
    
    for i in range(length):
        more = False
        
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                #one way to swap elements in array
                swap(arr, j, j + 1)
                more = True
                
        if not more: #array already sorted
            break

    if reverse:
        reverse_arr(arr)


def Insertion_sort(arr, reverse = False):
    length = len(arr)
    
    for i in range(length):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
            else:
                swap(arr, j, j - 1)

    if reverse:
        reverse_arr(arr)

def lomuto_partition(arr, left, right):
    pivot = arr[right]
    i = left - 1  #index point to larger element

    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)

    swap(arr, i + 1, right)

    return i + 1

def Quicksort(arr, left, right):
    if left < right:
        i = lomuto_partition(arr, left, right)
        Quicksort(arr, left, i - 1)
        Quicksort(arr, i + 1, right)


def Merge_sort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left_arr  = Merge_sort(arr[:mid])
        right_arr = Merge_sort(arr[mid:])

        left  = 0
        right = 0
        i     = 0
        
        while (left < len(left_arr)) and (right < len(right_arr)):
            if left_arr[left] <= right_arr[right]:
                arr[i] = left_arr[left]
                left += 1
            else:
                arr[i] = right_arr[right]
                right += 1

            i += 1

        while left < len(left_arr):
            arr[i] = left_arr[left]
            i     += 1
            left  += 1

        while right < len(right_arr):
            arr[i] = right_arr[right]
            i     += 1
            right += 1

    return arr
            
#=======================================================
#=======================================================
            
def test_bubble():
    arr = [4,6,3,5,1,3,4,0]
    Bubble_sort(arr)
    print(arr)
    Bubble_sort(arr, True)
    print(arr)

def test_insert():
    arr = [4,6,3,5,1,3,4,0]
    Insertion_sort(arr)
    print(arr)
    Insertion_sort(arr, True)
    print(arr)

def test_quick():
    arr = [4,6,3,5,1,3,4,0]
    Quicksort(arr, 0, len(arr) - 1)
    print(arr)

def test_merge():
    arr = [4,6,3,5,1,3,4,0]
    Merge_sort(arr)
    print(arr)
#=======================================================
#=======================================================

def linear_search(arr, num):
    for n in arr:
        if n == num:
            return True

    return False

def binary_search(arr, num):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return True

        elif arr[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    return False

#=======================================================
#=======================================================

def test2():
    arr = [4,6,3,5,1,3,4,0]
    print(linear_search(arr, 1))
    print(linear_search(arr, 10))
    print(linear_search(arr, 0))
    print('======')
    print(binary_search(arr, 0))
    print(binary_search(arr, 5))
    print(binary_search(arr, 6))
    print(binary_search(arr, 3))
    print(binary_search(arr, 4))
    print(binary_search(arr, 1))
    
#========================================================
#========================================================
    
