#======== some keys ========#
ascending  = lambda x, y: x <= y
descending = lambda x, y: x >= y

'''
in-place sort:
  no return (void)

key (default ascending):
  binary function to compare 2 elements
'''
def InsertionSort(arr, key = ascending):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            # largest in sorted
            if ( key(arr[j-1], arr[j]) ):
                break

            swap_elements(arr, j, j-1)


def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def test():
    arr1 = [9,6,4,6,26,1,0,8]
    InsertionSort(arr1)
    print(arr1)
