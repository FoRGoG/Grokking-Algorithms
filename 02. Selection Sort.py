def find_smallest(arr):
    smallest = arr[0] # для хранения наименьшего значения
    smallest_index = 0 # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest: # если текущее значение меньше наименьшего
            smallest = arr[i] # значит текущее значение становится наименьшим
            smallest_index = i # соответсвенно индекс текущего значения меняется
    return smallest_index # возвращаем наименьший индекс

def selectionSort(arr): # сортирует массив
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr) # находит наименьший элемент в массиве
        newArr.append(arr.pop(smallest)) # и добавляет его в новый массив
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([33, 21, 56, 122, 529, 4]))
