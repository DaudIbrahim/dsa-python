# flake8: noqa
"""
    Python List (Built in Data Structure)

    A - Access
    S - Search
    I - Insert
    D - Delete

    A - Accessing/Traversing a list
    S - Searching for an element in a List
    I - Update/Insert a List
    D - Slice/Delete from a List
"""

# Access/Traversing the list
my_list = ["Orange", "Cheese", "Butter"]
print("Orange" in my_list, "Milk" in my_list)

for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

# Update/Insert - List
integer_list = [1, 2, 3, 4, 5, 6, 7]
integer_list[2] = integer_list[2] * 10
integer_list.insert(2, 15)
integer_list.append(100)
integer_list.extend(["A", "B"])

# Slice/Delete from a List

# https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples#getting-sublists-with-slices
print("Slice", integer_list[0:4])


# https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples#removing-values
# pop, delete, remove.
integer_list.pop(len(integer_list) - 1)
del integer_list[len(integer_list) - 1]
integer_list.remove(100)

# Searching for an element in the list
target = 30

# In uses linear Search
if target in integer_list:
    print(f"{target} in list")
else:
    print(f"{target} is not in list")


def linear_search(p_list, p_target):
    # Linear Search
    for index, value in enumerate(p_list):
        if value == p_target:
            return index

    return -1


"""
    List Operations/Functions

    Lists and Strings

    Common List pitfalls and ways to avoid them

    Lists vs Arrays

    Time and Space Complexity of List
"""
# Concatenate Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

# * Operator
a = [0, 1]
a = a * 4

# length
len_of_a_list = len(integer_list[0:4])

max_integer = max(integer_list[0:3])
min_integer = min(integer_list[0:3])
sum_integer = sum(integer_list[0:3])

# Strings and Lists
my_string = "HelloWorld"
string_to_list = list(my_string)
string_split = my_string.split()
string_split_delimeter = "New-York-City".split("-")
string_join = ",".join(my_string)

# Common List pitfalls and ways to avoid them
# Be wary of working on making changes on reference vs value

"""
    List Comprehension & Conditional List Comprehension

    List Comprehension - List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    newlist = [expression for item in iterable if condition == True]

    https://www.w3schools.com/python/python_lists_comprehension.asp
"""

# String example with Conditional List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# newlist = [expression for item in iterable if condition == True]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [expression for expression in numbers if expression % 2 != 0]
even_multiplied = [(num * 2) for num in numbers if num % 2 == 0]
print(even_multiplied)

"""
    my_list Py
"""

my_list = [10, 20, 30, 40, 50]
print("\nmy_list", my_list)

# traversal | Accessing/Traversing a list
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

for index, item in enumerate(my_list):
    print(index, item)

i = 0

while i < len(my_list):
    print(i, my_list[i])
    i += 1

# insert/update |  { pop, remove } { append, insert }
my_list[0] = my_list[0] * my_list[0]
my_list.append(60)
my_list.pop(0)
my_list.insert(0, 10)
my_list.pop(len(my_list) - 1)
print(my_list)
print("\n")

# slicing | start:end
print(my_list[:])
print(my_list[0:2])
print("\n")

# stepper | start:stop:stepper
print("stepper", my_list[3:0:-1])
print(my_list[::2])
print(my_list[1::3])
print("\n")

# positive/negative indices
print(my_list[:1] + my_list[-1:])
print("\n")

# list Comprehensions
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [(item) for item in number_list if (item % 2 == 0)]
odd_list = [(item) for item in number_list if (item % 2 != 0)]

print(even_list, odd_list)

# End. Clear on Python Lists - synatx, looping, ASID, slicling & omprehension
## ACID stands for Atomicity, Consistency, Isolation, and Durability.
## Mmmory hook for me reagarding Data Structures
#   - ASID: Access, Search, Insert and Delete
