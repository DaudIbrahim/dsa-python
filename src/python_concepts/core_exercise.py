# flake8: noqa

from typing import List


# two_sum_enumerate
def two_sum_enumerate(nums: List[int], target: int):
    for idx, item in enumerate(nums):
        slice_idx = idx + 1
        for element_tuple in enumerate(nums[slice_idx:], slice_idx):
            if (item + element_tuple[1]) == target:
                return [idx, element_tuple[0]]
    return []


result = two_sum_enumerate([3, 21, 15, 7], 10)
print("two_sum_enumerate, result indices ->", result)


# The ultimate goal is to become proficient in the art of problem-solving. Do not get bogged down by language constructs; instead, focus your efforts on deeply understanding problems and devising elegant algorithms and solutions. Programming languages, in our case Python, is the tool to effectively implement those solutions. Conquer the essence of problem-solving first, and language constructs will naturally follow.


def two_sum_while(nums: List[int], target: int) -> List[int]:
    i = 0
    j = 1

    while i < len(nums):
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
        j = i + 1

    return []


result = two_sum_while([3, 21, 15, 7], 10)
print("two_sum_while, result indices ->", result)

print(list(range(12)))
