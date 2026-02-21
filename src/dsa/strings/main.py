# Strings in python

"""
Strings are immutable in python
The standard pattern for in-place-style manipulation in Python is:
Convert to a list, do your work, then join back
"""

# Converting to a list
string_one = "hello"
list_of_chars = list(string_one)

for item in list_of_chars:
    print(item, "\n")

# Join back
join_back_string = "".join(list_of_chars)
print(join_back_string, "\n")

# Frequency counting
freq = {}
for char in list_of_chars:
    freq[char] = freq.get(char, 0) + 1

print(freq)
