"""
This problem was provided by "https://www.dailycodingproblem.com/"
Day 1 : Given a List of numbers and a number k, return whether any two numbers
from the list add up to k.
For example : Given [10, 15, 3, 7] and k of 17, return since 10 + 7 is 17.
Bonus : Can you do this in one pass?
"""


def check_sum(list_1, num):
    for i in range(len(list_1) - 1):
        for j in range(i+1, (len(list_1))):
            if list1[i] + list1[j] == num:
                return True
    return False


def check_visited(list_1, num):
    visited_list = set()
    for item_ in list1:
        if num - item_ in visited_list:
            return True
        else:
            visited_list.add(item_)
    return False


list1 = []
a = int(input('Enter the no. of items in the list : '))
for item in range(a):
    b = int(input('Enter the element : '))
    list1.append(b)

number_to_be_checked = int(input('Enter the number to check sum : '))
a_ = check_sum(list1, number_to_be_checked)  # Method 1
b_ = check_visited(list1, number_to_be_checked)  # Method 2
