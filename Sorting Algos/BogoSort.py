# some keys
ascending  = lambda x,y : x < y
descending = lambda x,y : x > y

# The Ultimate Sort
def BogoSort(arr, key = ascending):
    all_permutations = permutate(arr)

    # find the sorted array from all possible permutations
    for permutation in all_permutations:
        if (is_sorted(permutation, key)):
            return permutation


# get all possible permutations of an array
def permutate(arr):
    output   = []
    main_len = len(arr)

    '''
    current: current array in the recursion
    counter: keeps of count of each found but unused numbers
    length:  length of current recured array
    '''
    def backtrack(current, counter, length):
        if length == main_len: # reached the last element
            output.append(list(current)) # add to output
            return
            
        for num in counter: # for each number alr found
            if counter[num] > 0:
                current.append(num) # add to a permutation
                counter[num] -= 1 # reduce count from "unused" 
                
                # recurse current permutation further
                backtrack(current, counter, length + 1)
                    
                current.pop() # remove added number
                counter[num] += 1 # add popped number back
        
    backtrack([], Counter(arr), 0)    
    return output

def Counter(arr):
    counter = dict()
    for each in arr:
        if (each not in counter):
            counter[each] = 0

        counter[each] += 1

    return counter

# check if an array is sorted by key
def is_sorted(arr, key):
    for i in range(len(arr) - 1):
        if ( key(arr[i + 1], arr[i]) ):
            return False

    return True

def test():
    arr1 = [7,4,6,2,1,9,3,2,5]
    print(BogoSort(arr1))
test()
