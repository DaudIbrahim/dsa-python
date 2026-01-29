# Merge Sort Implementation
# Standard Merge Sort

def getMidIndex(arr: [int], low: int, high: int) -> int:
    return low + ((high - low) // 2)


def merge(arr_one: list[int], arr_two: list[int]) -> list[int]:
    arr = []

    i = 0
    j = 0

    while (i < len(arr_one) and j < len(arr_two)):

        if (arr_one[i] <= arr_two[j]):
            arr.append(arr_one[i])
            i += 1
        else:
            arr.append(arr_two[j])
            j += 1

    # loop end
    if (i < len(arr_one)):
        for idx in range(i, len(arr_one)):
            arr.append(arr_one[idx])

    else:
        for idx in range(j, len(arr_two)):
            arr.append(arr_two[idx])

    return arr


def merge_sort(arr: list[int]) -> list[int]:

    # base case
    if (len(arr) <= 1):
        return arr

    # split left/right
    mid = getMidIndex(arr, 0, len(arr))
    left_half = merge_sort(arr[0:mid])
    right_half = merge_sort(arr[mid:len(arr)])

    # merge
    result = merge(left_half, right_half)

    # result
    return result
