# flake8: noqa
# One Dimensional Array

# https://learnpython.com/blog/python-array-vs-list/
# Arrays are not a built-in data structure, and therefore need to be imported via the array module in order to be used.

# Python Array Module
# https://docs.python.org/3/library/array.html

import array as arr

# Empty array of integer
my_array = arr.array("i", [10, 30])
print(my_array)

# Insertion
my_array.insert(1, 20)
print("Insert", my_array)


def traverse_an_array(array):
    # Traversal
    for element in array:
        print(element, "traverse")


def access_element(array, index):
    # Access an element of array
    if index > (len(array) - 1):
        print(f"Access Non-Existent Index: {index}, Array length equals {len(array)}")
    else:
        print(f"Access Element at Index {index} is equal to {array[index]}")


access_element(my_array, 2)


def linear_search(array, target):
    # Searching for an element in Array
    # Alternate way of looping
    for i in range(len(array)):
        if array[i] == target:
            return 1

    return -1


print("Search", linear_search(my_array, 30))


# Deleting an element from Array
my_array.remove(10)
print("delete", my_array)
