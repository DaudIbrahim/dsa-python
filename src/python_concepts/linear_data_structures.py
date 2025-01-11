# flake8: noqa

# Linear Data Structures Operations

# Lists []

# Lists are mutable and ordered collections, meaning you can change the elements after creation, and the order of elements is maintained.
# Python: Lists are ordered collections of elements that can contain items of any data type.
# They are mutable, meaning their elements can be changed after creation.

# Example: Adding elements to a list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("List after appending:", my_list)

# Example: Removing an element from a list
my_list.remove(3)
print("List after removing 3:", my_list)

# Example: List comprehension
squared_numbers = [x**2 for x in my_list]
print("Squared numbers:", squared_numbers)

# Example List slicing : https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples#getting-sublists-with-slices
print("Slice from index 1 to index 3 exclusive", my_list[1:3])
print("Slice from the beginning to index 3 exclusive", my_list[:3])
print("Slice with a step of 2", my_list[::2])

"""
// JavaScript Equivalent
// JavaScript: Arrays in JavaScript serve a similar purpose to lists in Python.
// They are ordered collections of elements, and like Python lists, they can contain elements of any data type.
// JavaScript arrays are also mutable.
// let myArray = [1, 2, 3, 4, 5];

// Example: Adding elements to an array
// myArray.push(6);
// console.log("Array after appending:", myArray);

// Example: Removing an element from an array
// myArray.splice(2, 1); // Removes one element at index 2
// console.log("Array after removing 3:", myArray);
"""

# Tuples ()

# Tuple: A general term for an ordered list of elements.
# 3-tuple (triple): A tuple with exactly three elements, e.g., (a, b, c).
# 4-tuple (quadruple): A tuple with exactly four elements, e.g., (a, b, c, d).
# tuples are read only - ()

# Tuples are immutable and ordered collections. Once created, their elements cannot be changed, added, or removed, but the order of elements is preserved.
# Python: Tuples are immutable ordered collections of elements.
# Once created, their elements cannot be changed.

# Example: Accessing elements of a tuple
my_tuple = (1, 2, 3, 4, 5)
print("First element of tuple:", my_tuple[0])

# Example: Attempting to modify a tuple (will result in an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# Example: Tuple comprehension (Not applicable; tuples are immutable and cannot be directly comprehended)

"""
// JavaScript Equivalent (Closest approximation)
// JavaScript: JavaScript does not have a direct equivalent to Python tuples.
// However, you can use arrays in JavaScript to achieve a similar structure by ensuring that the array is not modified after creation to mimic immutability.
// const myTuple = Object.freeze([1, 2, 3, 4, 5]); // Freezing the array to prevent modifications
"""

# Sets {}
# Sets are mutable and unordered collections of unique elements. Sets do not maintain the order of elements, and they ensure that each element is unique within the set.
# Python: Sets are unordered collections of unique elements.
# They are mutable and can be modified after creation.

# Example: Adding elements to a set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("Set after adding 6:", my_set)

# Example: Removing an element from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Example: Set comprehension
squared_set = {x**2 for x in my_set}
print("Squared set:", squared_set)

"""
// JavaScript Equivalent
// JavaScript: JavaScript's Set object is similar to Python sets.
// Sets are collections of unique values, and they can be iterated in insertion order.
// let mySet = new Set([1, 2, 3, 4, 5]);

// Example: Adding elements to a set
// mySet.add(6);
// console.log("Set after adding 6:", mySet);

// Example: Removing an element from a set
// mySet.delete(3);
// console.log("Set after removing 3:", mySet);
"""
