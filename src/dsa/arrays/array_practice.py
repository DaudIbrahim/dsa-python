# https://docs.python.org/3/library/array.html#module-array
import array as arr

# 1. Create an Array and Traverse
my_array = arr.array("i", [22, 33, 44, 55])
for element in my_array:
    print(element)

print("\n")

# 2. Access individual element through indexes
print(my_array[2], "\n")

# 3. Append to the array. (End)
my_array.append(66)

# 4. Insert to the array (Beginning)
my_array.insert(0, 11)

# 5. Extend Python Array
my_array.extend(arr.array("i", [77, 88]))

# 6. Append using fromlist
tempList = [99]
my_array.fromlist(tempList)

# 7. Remove using remove()
my_array.remove(99)

# 8. Remove using pop()
my_array.pop()

# 9. Fetch element using index method
print(my_array.index(22, 0, 5), "\n")

# 10 Reverse
my_array.reverse()

# 11 Get Array Buffer information
print(my_array.buffer_info(), "\n")

# 12 Check for number of occurence of an element
print(my_array.count(11), "\n")

# 13 Convert an Array to String
str_temp = my_array.tobytes()
my_ints = arr.array("i")
my_ints.frombytes(str_temp)
print(my_ints, "\n")

# 14 Array to list
print(my_array.tolist(), "\n")

# 15 Append a string to char array using fromString
# toString and fromString methods renamed to tobytes() and frombytes()
other_ints = arr.array("i", [50, 100])
other_ints.frombytes(arr.array("i", [150]).tobytes())
print(other_ints, "\n")

# 16 Slice
print(my_array[0:2], "\n")

# End
print(my_array)
