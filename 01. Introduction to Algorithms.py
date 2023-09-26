def binary_search(list, item):
    low = 0
    high = len(result) - 1 #4
    while low <= high: # пока эта часть не сократится до одного элемента
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item: 
            return mid
        if guess > item:
            high = low - 1
        else:
            low = mid + 1
    return None

result = [2, 4, 12, 33, 98]
print(binary_search(result, 33))
print(binary_search(result, 23))

