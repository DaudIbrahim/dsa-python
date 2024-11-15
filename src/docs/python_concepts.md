# Python Concepts

[YT Playlist Private](https://www.youtube.com/playlist?list=PLxvbXPxg6ydwnnFlNgGKYevGy6hQHBQzE)

This folder contains code related to various Python language concepts.

## 1. **Variables and Data Types:**

- [Python Variables and Data Types](https://www.w3schools.com/python/python_variables.asp)

```python
# Variables and Data Types
x = 42
name = "John"
my_list = [1, 2, 3]
my_dict = {"key": "value"}
```

## 2. **Control Flow:**

- [Python Control Flow Statements](https://docs.python.org/3/tutorial/controlflow.html)

```python
# Control Flow
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

for item in my_list:
    print(item)

while condition:
    # code
```

## 3. **Loops:**

Loops in Python are used to repeatedly execute a block of code until a certain condition is met. There are mainly two types of loops in Python: `for` and `while`.

### 3.1 For Loop

The `for` loop in Python is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). Here's a basic example:

```python
# For Loop
for item in my_list:
    print(item)
```

`for` loop using `range`:

```python
for i in range(5):
    print(i)
```

`for` loop using `enumerate`:

```python
list = ["A", "B", "C"]

# The enumerate() function in Python accepts an optional second argument, which sets the starting value for the index. In your code, the second argument is 10, so indexing begins from 10. Consequently, the first element in the list receives an index of 10, the second element an index of 11, and so forth
for index, item in enumerate(list, start = 10):
    print(index, item)

```

### 3.2 While Loop

The `while` loop is used to repeatedly execute a block of code as long as the given condition is true. Here's an example:

```python
# While Loop
i = 0
while i < 5:
    print(i)
    i += 1
```

This `while` loop prints the numbers 0 to 4. The loop continues as long as the condition `i < 5` is true.

Python does not have traditional C-style for loops. You can rewrite every `for` loop as a `while` loop, and vice versa. The two types of loops are equivalent in terms of expressive power, meaning that any computation that can be done with one can also be done with the other.

Here's a simple example in Python to illustrate the equivalence:

Using a `for` loop:

```python
# Python does not have traditional C-style for loops.
# https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python
for i in range(5):
    print(i)
```

Equivalent `while` loop:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

In both cases, the loop will print the numbers 0 to 4. The `for` loop is often more concise and readable for situations where you know the number of iterations in advance. On the other hand, the `while` loop can be more flexible when the termination condition is not based on a fixed range.

### 3.3 Do While Loop (Emulation)

[Python does not have built-in functionality to explicitly create a do while loop like other languages. But it is possible to emulate a do while loop in Python.](https://www.freecodecamp.org/news/python-do-while-loop-example/)

Python does not have a built-in `do while` loop, but it can be emulated using a `while` loop. Here's an example:

```python
# Emulating Do While Loop
while True:
    print(f"Number is {number}!")
    if number >= 10:
        break
```

This loop will execute the code block at least once and then continue as long as the condition is true.

Loops are fundamental for iterating through data structures, processing elements, and implementing repetitive tasks in your Python programs.

## 4. **Functions:**

- [Defining Functions in Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

```python
# Functions
def add_numbers(a, b=0):
    return a + b

result = add_numbers(5, 3)
```

## 5. **[Lists, Sets and Tuples](https://youtu.be/gOMW_n2-2Mw):**

- [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Tuples](https://docs.python.org/3/tutorial/introduction.html#tuples-and-sequences)

```python
# Lists and Tuples
my_list = [1, 2, 3, 4]
my_set = {1, 2, 3}
my_tuple = (1, 2, 3)

print(my_list[0])  # Accessing elements
print(my_list[1:3])  # Slicing
my_list.append(5)  # Appending

# push()   ->   append()
# pop()    ->   pop()

# shift()  ->   pop(0) or del list[0]
# unshift() ->   [element] + list_name
```

## 6. **Dictionaries:**

- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

```python
# Dictionaries
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key1"])
```

## 7. **List Comprehensions:**

- [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

```python
# List Comprehensions
squares = [x**2 for x in range(5)]
```

## 8. **Exception Handling:**

- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

```python
# Exception Handling
try:
    # code that might raise an exception
except SomeException as e:
    # handle the exception
finally:
    # optional, always executed
```

## 9. **Classes and Objects:**

- [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)

```python
# Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")
```

## 10. **Recursion:**

- [Recursion in Python](https://realpython.com/python-thinking-recursively/)

```python
# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

## 11. **Sorting:**

- [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

```python
# Sorting
my_list = [4, 2, 8, 1]
sorted_list = sorted(my_list)
```

## 12. **Lambda Functions:**

- [Lambda, filter, reduce, and map](https://towardsdatascience.com/python-map-reduce-lambda-and-list-comprehensions-61901f47b7f6)

```python
# Lambda Functions
add = lambda x, y: x + y
result = add(3, 5)
```

## 13. **Generators:**

- [Python Generators](https://realpython.com/introduction-to-python-generators/)

```python
# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```
