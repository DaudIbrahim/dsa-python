# flake8: noqa

# input/output
input = [3, 21, 15, 7]
input_target = 10

# two_sum


def two_sum(nums: list[int], target: int):
    len_nums = len(nums)

    for i in range(0, len_nums):
        for j in range(i+1, len_nums):
            if (target == (nums[i] + nums[j])):
                return [i, j]

    return []


# print("two_sum ->", two_sum(input, input_target))


# The ultimate goal is to become proficient in the art of problem-solving. Do not get bogged down by language constructs; instead, focus your efforts on deeply understanding problems and devising elegant algorithms and solutions. Programming languages, in our case Python, is the tool to effectively implement those solutions. Conquer the essence of problem-solving first, and language constructs will naturally follow.


def two_sum_while(nums: list[int], target: int) -> list[int]:
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


# print("two_sum_while ->", two_sum_while(input, input_target))

# twoSum: hashMap


def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    hash_map = dict()

    # we use compliment
    for idx in range(len(nums)):
        val = nums[idx]
        compliment = target - val

        if (compliment in hash_map):
            return [idx, hash_map.get(compliment)]
        else:
            hash_map[val] = idx

    return []


print("two_sum_hash_map ->", two_sum_hash_map([3, 2, 4], 6))
print("two_sum_hash_map ->", two_sum_hash_map([3, 3], 6))
