# Merge Two Sorted Arrays
# Given two sorted arrays, merge them into one sorted array

def merge_two_sorted_arrays(arr_one: list[int], arr_two: list[int]) -> list[int]:
    """
    Merges two sorted arrays into one sorted array.

    Args:
        arr_one: First sorted array
        arr_two: Second sorted array

    Returns:
        A new sorted array containing all elements from both input arrays

    Example:
        merge_two_sorted_arrays([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
    """

    arr = []

    pointer_one = 0
    length_one = len(arr_one)

    pointer_two = 0
    length_two = len(arr_two)

    while (pointer_one < length_one and pointer_two < length_two):

        # <=
        # lesss than or equal to
        # makes the algorithm stable
        if (arr_one[pointer_one] <= arr_two[pointer_two]):
            arr.append(arr_one[pointer_one])
            pointer_one += 1
        else:
            arr.append(arr_two[pointer_two])
            pointer_two += 1

    for i in range(pointer_one, length_one):
        arr.append(arr_one[i])

    for j in range(pointer_two, length_two):
        arr.append(arr_two[j])

    return arr
