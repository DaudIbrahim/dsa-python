"""
The 3Sum problem requires examining all possible combinations
of three elements in the array,and this involves nested iterations.
Therefore, the time complexity of any algorithm solving the 3Sum problem
is lower-bounded by O(n^2), where "n" is the length of the array.
"""


def find_sum_of_three(nums, target):
    low = 0
    high = len(nums) - 1
    pivot = low + 1

    nums.sort()
    print(nums)

    while low < high and pivot < high:
        current_sum = nums[low] + nums[pivot] + nums[high]

        if current_sum == target:
            return True
        elif current_sum > target:
            high -= 1
        else:
            # check each combination, spent a lot time figuring this.
            diff = pivot - low
            if diff == 1:
                pivot += 1
            else:
                low += 1

    return False


def find_sum_of_three_alternate(nums, target):
    # Sort the input array
    nums.sort()

    # Iterate through the array
    for i in range(len(nums) - 2):
        # Initialize pointers
        low = i + 1
        high = len(nums) - 1

        # Adjust pointers based on current sum
        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]

            if current_sum == target:
                return True
            elif current_sum < target:
                low += 1
            else:
                high -= 1

    # No triplet found
    return False
