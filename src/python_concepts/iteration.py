# flake8: noqa

# memory hook for loops in python - while-forIn-range-enumerate - WFRE

from typing import List

my_list: List[int] = [10, 20, 30]

# while loop
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# for...in loop
for item in my_list:
    print(item)

# Python does not support traditional for loops with an index directly like in JavaScript.
# Instead, we use the range() function to create a sequence of indices.
# range-based for loop (similar to traditional for loop with index in other languages)
for i in range(len(my_list)):
    print(my_list[i])


# for...in Iterates over the keys (or values) of an iterable object such as a list, tuple, dictionary, or set.
# enumerate loop
for index, item in enumerate(my_list):
    print(index, item)

# Iterating through a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(key, value)
