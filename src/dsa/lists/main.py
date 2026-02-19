"""
    Lists in Python
"""

arr = [10, 20, 30, 40, 50]
print("arr", arr)

# traversal | Accessing/Traversing a list
for item in arr:
    print(item)

for i in range(len(arr)):
    print(arr[i])

i = 0
while i < len(arr):
    print(i, arr[i])
    i += 1

# add/remove from end of list
arr.append(60)
arr.pop()

# add/remove from start | use deque for O(1) performance
arr.insert(0, 1)
arr.pop(0)

# remove first occurrence of value — raises ValueError if not found
if 60 in arr:
    arr.remove(60)

# slicing | start:stop  (stop is exclusive)
print(arr[:])       # full copy
print(arr[0:2])     # index 0 and 1

# stepper | start:stop:step
print(arr[3:0:-1])  # index 3 down to 1
print(arr[::2])     # every other element
print(arr[::-1])    # reverse

# positive/negative indices
print(arr[:1] + arr[-1:])   # first + last element

# list comprehensions
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [item for item in number_list if item % 2 == 0]
odd_list = [item for item in number_list if item % 2 != 0]
print(even_list, odd_list)

# leetcode helpers
arr.sort()                  # in-place ascending sort
arr.sort(reverse=True)      # in-place descending sort
new_arr = sorted(arr)       # returns new sorted list, original unchanged

print(len(arr))             # length
print(min(arr), max(arr))   # min and max
print(sum(arr))             # sum

arr.reverse()               # reverse in-place
print(arr.count(10))        # count occurrences of value
# index of first occurrence — raises ValueError if not found
print(arr.index(40))
