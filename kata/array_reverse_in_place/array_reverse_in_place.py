# length and index are distinct
# length -> working with counts, counting world
# index -> working with indices, index world
# in both case making use of Half open interval

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
    right = len(nums)

    while (left < right):
        nums[left], nums[right - 1] = nums[right - 1], nums[left]
        left += 1
        right -= 1

    return nums


def reverse_in_place_index_mirroring(nums: list[int]) -> list[int]:
    """
    Reverse an array in place using index mirroring.

    The elegance here comes from two ideas reinforcing each other:
    integer division and half-open intervals are two sides of the same coin.

    mid = len(nums) // 2  floors toward the midpoint boundary.
    range(0, mid) says "up to but not including mid" — half-open.

    The same value that counts our swap pairs is also the exclusive
    upper bound for the loop. Odd arrays leave the middle element
    untouched, and floor division quietly accounts for that by not
    counting it as a pair. No special casing needed. It just works.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # length and index are distinct mental models
    # length -> counting world
    # index  -> index world
    # both make use of the half open interval [left, right)
    length = len(nums)
    left = 0
    right = len(nums)  # half open: right is exclusive
    mid = left + ((right - left) // 2)

    # mid = len(nums) // 2  ->  integer division "rounds down"
    # this gives us the number of swap pairs in both even and odd cases:
    #   even: [1,2,3,4] -> 2 pairs -> swap indices (0,3) and (1,2)
    #   odd:  [1,2,3]   -> 1 pair  -> swap indices (0,2), middle element stays
    #
    # the same value that counts our pairs also happens to be
    # the exclusive upper bound we need for range()
    # so range(0, mid) gives us exactly the right number of iterations
    for i in range(0, mid):
        nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]

    return nums
