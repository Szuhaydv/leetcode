arr = [1, 2, 3]

def sum(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + sum(array[1:])

def count(array):
    if not array:
        return 0
    elif len(array) == 1:
        return 1
    else:
        return 1 + count(array[1:])

def rec_maximum(array):
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], rec_maximum(array[1:]))

def rec_binary_search(array, entry):
    if not array:
        return None
    middle = (len(array) - 1) // 2
    middleElem = array[middle]
    if middleElem == entry:
        return entry
    elif middleElem < entry:
        return rec_binary_search(array[middle+1:], entry)
    else:
        return rec_binary_search(array[:middle], entry)
        

print("Sum:", sum(arr))
print("Count:", count(arr))
print("Maximum:", rec_maximum(arr))
print("Search 2 in [1,2,3]:", rec_binary_search(arr, 2))
print("Search 4 in [1,2,3]:", rec_binary_search(arr, 4))
