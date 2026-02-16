# length and index are distinct
# length -> working with counts, counting world
# index -> working with indices, index world

def reverse_in_place_two_pointers(nums: list[int]) -> list[int]:
    """
    Reverse an array in place using two pointers approach.

    Args:
        nums: A list of integers to reverse

    Returns:
        The same list reversed (modified in place)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(nums) - 1

    while (left < right):
        # swap
        nums[left], nums[right] = nums[right], nums[left]

        # pointers
        left += 1
        right -= 1

    return nums


def reverse_in_place_index_mirroring(nums: list[int]) -> list[int]:
    """
    Reverse an array in place using index mirroring approach.

    Args:
        nums: A list of integers to reverse

    Returns:
        The same list reversed (modified in place)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    length = len(nums)
    mid = 0 + ((length - 0) // 2)

    for i in range(0, mid):
        nums[i], nums[length - 1 - i] = nums[length - 1 - i], nums[i]

    return nums
