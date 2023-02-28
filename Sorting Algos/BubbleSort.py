#======== some keys ========#
ascending  = lambda x, y: x <= y
descending = lambda x, y: x >= y


'''
in-place sort:
  no return (void)
  
key (default ascending):
  binary function comparing 2 arguments
  returns boolean
'''
def BubbleSort(arr, key = ascending):
    swap = False
    arr_length = len(arr) - 1
    
    for i in range(arr_length):
        swap = False
        
        for j in range(arr_length - i):
            if (not key(arr[j], arr[j+1]) ):
                swap_elements(arr, j, j+1)
                swap = True

        if (not swap): # elements already in order
            break


def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def test():
    arr1 = [9,5,2,1,5,7,3,7,8,0]
    BubbleSort(arr1)
    print(arr1)
