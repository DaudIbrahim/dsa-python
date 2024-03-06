from typing import List

myList = [10, 20, 30, 40, 50]
myTuple = (10, 20, 10)
mySet = {"A", "B", "C"}

# loop #1 for_in
for item in myList:
    print(item)

# loop #2 range
for i in range(len(myList)):
    print(item, "range")

# loop #3 enumerate
for index, item in enumerate(myList, start=10):
    print(index, item, "enumerate")

# loop #4 while
i = 0
while i < len(myList):
    print(myList[i], "while")
    i += 1

# comprehension
print([item for item in myList if item >= 30])

# slicing. start:end:stepper
print("\n")
print(myList[:])
print(myList[-1::-1])


# two_sum_for_loop
def two_sum_for_loop(nums: List[int], target: int):
    for idx, item in enumerate(nums):
        slice_idx = idx + 1
        for element_tuple in enumerate(nums[slice_idx:], slice_idx):
            if (item + element_tuple[1]) == target:
                return [idx, element_tuple[0]]
    return []


result = two_sum_for_loop([2, 7, 11, 15], 9)
print("two_sum_for_loop, result indices ->", result)
