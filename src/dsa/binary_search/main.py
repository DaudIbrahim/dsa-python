# https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/
# int mid = (low + high) >>> 1;
# for integer division use //
def getMidIndex(arr: [int], lowInclusive: int, highExclusive: int) -> int:
    return lowInclusive + ((highExclusive - lowInclusive) // 2)


# Binary Search Implementation
def binary_search(arr: list[int], target: int) -> int:

    # inclusive low
    low = 0

    #  exclusive high
    high = len(arr)

    # loop
    while (low < high):
        # mid
        mid = getMidIndex(arr, low, high)

        if (target == arr[mid]):
            return mid
        elif (target < arr[mid]):
            low = low
            high = mid
        elif (target > arr[mid]):
            low = mid + 1
            high = high

    return -1
