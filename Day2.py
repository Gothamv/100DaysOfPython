'''
Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.
For example : If input = [3, 2, 1] , output would be [2, 3, 6]
Bonus : What if division is not allowed?
'''


def with_divison(array_):
    result = 1
    for num in array_:
        result *= num
    list_ = [result // num for num in array_]
    return list_


def without_division(arr):
    l = len(arr)
    list_ = []
    for i in range(l):
        product = 1
        for j in range(l):
            if i is not j:
                product *= arr[j]
        list_.append(product)
    return list_


array = [1, 2, 3, 4, 5]
print(with_divison(array))
print(without_division(array))
