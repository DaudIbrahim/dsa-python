from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if (nums[i] >= target):
                return i

        return len(nums)


# init solution
sol = Solution()

nums = [-1, 3, 5, 6]
target = 0

result = sol.searchInsert(nums, target)
print(result)
