def build_prefix_sum_normal(nums: list[int]) -> list[int]:
    """
    Build a prefix sum array using the normal (index-aligned) model.
    The result has the same length as the input array (length n).

    prefix[i] = sum of elements from index 0 to i (inclusive)

    Example:
        arr    = [2, 5, 3, 7]
        prefix = [2, 7, 10, 17]

    Interpretation:
        prefix[0] = 2          -> just arr[0]
        prefix[1] = 2 + 5 = 7  -> arr[0] + arr[1]
        prefix[2] = 7 + 3 = 10 -> arr[0] + arr[1] + arr[2]
        prefix[3] = 10 + 7 = 17-> arr[0] + arr[1] + arr[2] + arr[3]

    Range query — sum of indices l to r inclusive:
        if l == 0:
            prefix[r]
        else:
            prefix[r] - prefix[l - 1]

    Note the edge case: when l == 0, there is nothing to subtract,
    so we must branch. This is the main limitation of this model.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # empty
    if not (nums):
        return []

    # prefix_sum_normal implementation
    prefix_sum_normal = [nums[0]]

    for i in range(1, len(nums)):
        current_sum = nums[i] + prefix_sum_normal[i - 1]
        prefix_sum_normal.append(current_sum)

    return prefix_sum_normal


def build_prefix_sum_zero_offset(nums: list[int]) -> list[int]:
    """
    Build a prefix sum array using the zero-offset (counting world) model.
    The result has length n+1, one longer than the input array.

    P[0] = 0
    P[i] = sum of first i elements = a0 + a1 + ... + a(i-1)

    Example:
        arr = [2, 5, 3, 7]
        P   = [0, 2, 7, 10, 17]

    Interpretation:
        P[0] = 0  -> sum of 0 elements
        P[1] = 2  -> sum of first 1 element
        P[2] = 7  -> sum of first 2 elements
        P[3] = 10 -> sum of first 3 elements
        P[4] = 17 -> sum of first 4 elements

    The index into P measures "how many elements are included",
    not "which array index". This is the counting world shift.

    Range query — sum of indices l to r inclusive:
        P[r + 1] - P[l]

    No edge case. No branching. Always the same formula.
    This is why zero-offset is the superior model.

    Core identity:
        P[b] - P[a] = sum of elements at indices a through b-1

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # empty
    if not (nums):
        return [0]

    # prefix_sum_zero_offset implementation
    prefix_sum_zero_offset = [0, nums[0]]

    for i in range(1, len(nums)):
        current_sum = nums[i] + prefix_sum_zero_offset[i]
        prefix_sum_zero_offset.append(current_sum)

    return prefix_sum_zero_offset
