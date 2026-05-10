from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x,y: x+y,numbers)
print("the sum of the list is:",result)