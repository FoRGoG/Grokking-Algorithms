from functools import reduce

"""map function"""
arr1 = [1, 2, 3, 4, 5]
arr2 = list(map(lambda x: 2*x, arr1))
print(arr2)

"""reduce function"""
arr3 = [1, 2, 3, 4, 5]
result = reduce(lambda x,y: x+y, arr3)
print(result)