# Bubble Sort Implementation
def bubble_sort(arr: list[int]) -> list[int]:

    # Should not modify the original array
    nums = arr.copy()

    # invariant
    length = len(nums)

    # note: in range(0, length) | length is exclusive
    for i in range(0, length):

        is_swapped = False

        for j in range(0, length - 1 - i):

            # swap
            if (nums[j] > nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                is_swapped = True

        if (not is_swapped):
            break

    return nums
