# flake8: noqa

from typing import List

# Python lists, sets, and tuples explained 🍍
# https://youtu.be/gOMW_n2-2Mw?si=nKt34zfJHm57hhQo

# list - []
my_list = [10, 20, 30]

# Tuple: A general term for an ordered list of elements.
# 3-tuple (triple): A tuple with exactly three elements, e.g., (a, b, c).
# 4-tuple (quadruple): A tuple with exactly four elements, e.g., (a, b, c, d).
# tuples are read only - ()
my_tuple = (1, 2, 3)

# set are for unique elements - {}
my_set = {5, 6, 7}

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, value)
