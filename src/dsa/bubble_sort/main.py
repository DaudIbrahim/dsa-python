# Bubble Sort
def bubble_sort_initial(nums: list[int]) -> list[int]:

    count = len(nums) - 1

    while (count > 0):

        swapped = False

        for i in range(0, count):

            # swap
            if (nums[i] > nums[i + 1]):
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                swapped = True

        count -= 1

        if (not swapped):
            break

    return nums


def bubble_sort(nums: list[int]) -> list[int]:

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


# print(bubble_sort_initial([2, 3, 1]))
print(bubble_sort([2, 3, 1]))
