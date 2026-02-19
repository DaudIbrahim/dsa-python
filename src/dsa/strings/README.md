# Strings in Python

## Problem Set (Strings)

- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

- [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)
  - [Array reverse in place](../../../kata/array_reverse_in_place/array_reverse_in_place.py)

## The Big Similarity: Python Strings Are Also Immutable

Just like JavaScript, Python strings are immutable. Once created, you cannot modify a string in place. This is the single most important thing to internalize, because it shapes _every_ decision you make when manipulating strings in Python.

Think of a Python string as a read-only array of characters. You can read from it freely (index, slice, iterate), but to "modify" it, you produce a new string or go through a list as an intermediary.

```python
s = "hello"
s[0] = "H"  # ❌ TypeError: 'str' object does not support item assignment
```

## Converting between strings and lists

Since strings are immutable, the standard pattern for in-place-style manipulation in Python is: **convert to a list, do your work, then join back**.

```python
s = "hello"
chars = list(s)         # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'          # lists ARE mutable
result = "".join(chars) # "Hello"
```

You'll use `list(s)` + `"".join(...)` constantly in LeetCode problems. Burn this pattern into your memory.

## String concatenation in loops — a trap

Since strings are immutable, doing `s += char` inside a loop creates a brand new string every iteration. This is O(n²) time in the worst case. The fix is to accumulate into a list and join at the end.

```python
# ❌ Slow — O(n²)
result = ""
for char in chars:
    result += char

# ✅ Fast — O(n)
result = "".join(chars)
```

### Why it's O(n²)

- Strings in Python are **immutable**.
- `s += char` creates a **new string every time**.
- Each time, Python copies the whole old string → **O(k)** at step `k`.
- Doing that `n` times gives:
  `0 + 1 + 2 + ... + n` → **O(n²)**.

Use this instead:

```python
res = []
for c in s:
    res.append(c)

final = "".join(res)  # O(n)
```

That's it.

## String Methods You MUST Know for LeetCode

All slicing syntax applies to strings:

```text
s[start : stop : step]

s[::-1]   # reverses the string — use this for palindrome problems
```

```python
s = "Hello World"

# Case
s.lower()             # "hello world" — normalize before comparing
s.upper()             # "HELLO WORLD"

# Search
s.find("World")       # 6    — index of first match, -1 if not found
s.count("l")          # 3    — count occurrences

# Check
s.startswith("Hello") # True
s.endswith("World")   # True
"World" in s          # True — simplest membership check

# Classification
"abc".isalpha()       # True — only letters
"123".isdigit()       # True — only digits
"a1".isalnum()        # True — letters or digits ← use this in palindrome problems
"12".isnumeric()      # True — like isdigit but also handles ², ½, etc.
" ".isspace()         # True

# Transform
s.strip()             # removes leading & trailing whitespace
s.replace("l", "r")   # "Herro Worrd"
s.split(" ")          # ["Hello", "World"]
s.split()             # same, but handles any whitespace

# ASCII — essential for problems involving character offsets
ord('a')              # 97  — char → number
chr(97)               # 'a' — number → char
ord('c') - ord('a')   # 2   — maps 'c' to index 2 in a 26-slot array

# Convert
my_list = list(s)
my_string = " ".join(my_list)
```
