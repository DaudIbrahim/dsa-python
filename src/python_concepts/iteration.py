# flake8: noqa

# memory hook for loops in python - while-forIn-range

from typing import List

my_list: List[int] = [10, 20, 30]

# while
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# for...in
# for...in iterates over the keys (or values) of an iterable object such as a list, tuple, dictionary, or set.
for item in my_list:
    print(item)

# range
# Python does not support traditional for loops with an index directly like in JavaScript.
# Instead, we use the range() function to create a sequence of indices.
# range-based for loop (similar to traditional for loop with index in other languages)
for i in range(len(my_list)):
    print(my_list[i])
