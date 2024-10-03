def quicksort(list):
    if len(list) < 2:
        return list

    pivot = list[0]

    smaller = [i for i in list[1:] if i <= pivot]
    larger = [i for i in list[1:] if i > pivot]

    return quicksort(smaller) + [pivot] + quicksort(larger)

test_list = [3, 4, 2, 1, 6, 7, 8, 5]
print(quicksort(test_list))
