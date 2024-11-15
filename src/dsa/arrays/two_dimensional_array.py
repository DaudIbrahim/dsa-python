# flake8: noqa
# Two Dimensional Array
# For 2D Arrays you can think of Database Table: Rows and Columns

# Create | Create the 2D Data Structure
# Traversal | Traverse the Data Structure

# Accessing | Access Element
# Searching | Searching Element
# Insertion | Insert Element
# Deletion | Deleting Element

# Arrays are not a built-in data structure, and therefore need to be imported via the array module in order to be used.
# https://learnpython.com/blog/python-array-vs-list/

# Python Array Module
# https://docs.python.org/3/library/array.html

import numpy as np

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9
# Create Two Dimensional Array
two_d_array = np.array(
    [
        [11, 15, 10, 9],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9],
    ]
)

print(two_d_array, "\n")

# Insertion - Two Dimensional Array
#
# Insertion: Adding Column
# Time Complexity = O(mn)
# m -> columns, n -> rows
#
# Insertion: Adding Row
# Time Complexity = O(mn)
# m -> columns, n -> rows
#
# https://numpy.org/doc/stable/reference/generated/numpy.insert.html
new_two_d_array = np.insert(two_d_array, 0, np.array([[1, 2, 3, 4]]), axis=0)
array_axis_1 = np.append(two_d_array, np.array([[6], [7], [8], [9]]), axis=1)
array_axis_0 = np.append(two_d_array, np.array([[0, 1, 2, 3]]), axis=0)


def access_element(array, row_index, col_index):
    # Accessing an element of Two Dimensional Array
    invalid_index = row_index >= len(array) or col_index >= len(array[0])
    assert (invalid_index) == False, "Invalid Index"
    return array[row_index, col_index]


def traverse_two_d_array(array):
    # Traversal - Two Dimensional Array
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i, j])


def search_element_in_two_d_array(array, value):
    # Searching for an element in Two Dimensional Array
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i, j] == value:
                return "Value is located at " + str(i) + " " + str(j)

    return "Value Not Found"


# Deletion - Two Dimensional Array
# axis = 0 (Row)
# axis = 1 (Column)
new_to_delete_array = np.delete(two_d_array, 0, axis=1)
print(new_to_delete_array, "\n")
