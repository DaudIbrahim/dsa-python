# flake8: noqa

# Comprehensions in Python
# Python Comprehensions - https://www.pythoncheatsheet.org/cheatsheet/comprehensions
# new_list = [expression for item in iterable if condition]

# In plain, everyday English, the word "comprehension" means understanding or grasping something fully.
# It involves the ability to comprehend or make sense of information.

# In programming, particularly in Python, "comprehension" refers to a concise way of constructing a new data structure by understanding existing data.
# It's like creating something new based on your understanding of what already exists.

# List Comprehension Example
squared_numbers = [x**2 for x in range(1, 6)]  # Result: [1, 4, 9, 16, 25]
print("squared_numbers", squared_numbers)

# Set Comprehension Example
squared_numbers_set = {x**2 for x in range(1, 6)}  # Result: {1, 4, 9, 16, 25}
print("squared_numbers_set", squared_numbers_set)


# Dictionary Comprehension Example
squared_numbers_dict = {
    x: x**2 for x in range(1, 6)
}  # Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("squared_numbers_dict", squared_numbers_dict)
