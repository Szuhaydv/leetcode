def binary_search(list, entry):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = (low + high) // 2
        if list[middle] == entry:
            return middle
        elif list[middle] < entry:
            low = middle + 1
        else:
            high = middle - 1
    return None
