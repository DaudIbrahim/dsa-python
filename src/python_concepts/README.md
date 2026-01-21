# PYTHON FOR DSA — BASIC CONCEPTS

## Looping

### while

```python
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1
# Output: Count is: 0, 1, 2, 3, 4
```

### for in

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry
```

### range()

```python
# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8

# Common usage
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

### enumerate()

```python
# Returns index and value pairs
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")
# Output: Index 0: Alice, Index 1: Bob, Index 2: Charlie

# With custom start index
# Gotcha: The second argument to enumerate sets the starting value for the index,
# but it does not change the fact that enumerate always starts iterating from
# the first element of the list. To skip elements, additional slicing or logic is needed.
for index, name in enumerate(names, start=1):
    print(f"Person {index}: {name}")
# Output: Person 1: Alice, Person 2: Bob, Person 3: Charlie
```

## Linear Data Structures

### list

```python
# mutable, ordered
# LISTS - most common in Leetcode
lst = [1, 2, 3, 4, 5]

# Access
lst[0]              # first element
lst[-1]             # last element
lst[1:3]            # slice [2, 3]

# Modify
lst.append(6)       # add to end - O(1)
lst.pop()           # remove last - O(1)
lst.insert(0, 99)   # insert at index - O(n)
lst.remove(3)       # remove first occurrence - O(n)

# Common patterns
len(lst)            # length
lst.reverse()       # reverse in place
lst.sort()          # sort in place
sorted(lst)         # return new sorted list
lst.count(2)        # count occurrences
```

### tuple

```python
# TUPLES - immutable, ordered, mostly for reading
tup = (1, 2, 3)

# Access (same as list)
tup[0]              # first element
tup[-1]             # last element

# Common use
x, y = (1, 2)       # unpacking
return (i, j)       # return multiple values
```

### string

```python
# immutable, ordered sequence of characters
my_string = "Hello World"
print(my_string[0])  # H
print(my_string.upper())  # HELLO WORLD
print(my_string.split())  # ['Hello', 'World']
```

## Non-Linear Data Structures

### set

```python
# unordered, for uniqueness and fast lookup
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.add(3)  # Duplicate, won't be added
s.discard(2)        # remove (no error if missing) - O(1)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))  # {3, 4}
print(set_a.difference(set_b))  # {1, 2}

# Check membership
5 in s              # O(1) - THIS IS KEY!
```

### dictionary

```python
# DICTIONARY - for fast key lookup
# key-value pairs, unordered
d = {"a": 1, "b": 2, "c": 3}

# Access
d["a"]              # get value (error if missing)
d.get("a")          # get value (None if missing)
d.get("z", 0)       # get with default value

# Modify
d["d"] = 4          # add/update - O(1)
del d["a"]          # remove key
d.pop("b")          # remove and return value

# Check
"a" in d            # check if key exists - O(1)

# Iterate
for key in d:                    # iterate keys
for value in d.values():         # iterate values
for key, value in d.items():     # iterate pairs

# Common patterns
d = {}
d[key] = d.get(key, 0) + 1      # count frequency
```

## Must-Know Operations

### indexing, slicing

```python
arr = [10, 20, 30, 40, 50, 60]

# Indexing
print(arr[0])   # 10 (first element)
print(arr[-1])  # 60 (last element)
print(arr[-2])  # 50 (second last)

# Slicing [start:stop:step]
print(arr[1:4])    # [20, 30, 40]
print(arr[:3])     # [10, 20, 30]
print(arr[3:])     # [40, 50, 60]
print(arr[::2])    # [10, 30, 50] (every 2nd element)
print(arr[::-1])   # [60, 50, 40, 30, 20, 10] (reverse)
```

### len()

```python
arr = [10, 20, 30, 40, 50, 60]
print(len(arr))           # 6
print(len("hello"))       # 5
print(len({"a": 1, "b": 2}))  # 2
```

### append(), pop()

```python
stack = [1, 2, 3]

# append() - adds to end
stack.append(4)
print(stack)  # [1, 2, 3, 4]

# pop() - removes and returns last element
last = stack.pop()
print(last)   # 4
print(stack)  # [1, 2, 3]

# pop(index) - removes at specific index
stack.pop(0)  # Removes first element
print(stack)  # [2, 3]
```

### in keyword

```python
# Check membership
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(10 in numbers)     # False

word = "hello"
print('e' in word)       # True
print('z' in word)       # False

my_dict = {"a": 1, "b": 2}
print("a" in my_dict)    # True (checks keys)
print(1 in my_dict)      # False (doesn't check values)
```

### dict.get()

```python
student = {"name": "Bob", "age": 20}

# Using [] - raises KeyError if key doesn't exist
# print(student["grade"])  # KeyError

# Using get() - returns None or default value
print(student.get("grade"))           # None
print(student.get("grade", "N/A"))    # N/A (default value)
print(student.get("name"))            # Bob

# Safe access pattern
grade = student.get("grade", 0)
print(f"Grade: {grade}")  # Grade: 0
```
