from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(0, len(nums)):
#             if (nums[i] >= target):
#                 return i

#         return len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Think About Invariants
        # An invariant is something that's always true during your loop:

        # low is our answer by default
        # if no element found larger than target
        # it means target itself is the smallest
        low = 0

        # high is exclusive
        # this will result if our element itself is the largest
        # then low will equal high
        # and since high is exclusive and low == high
        # in end low index will be equal to len(nums)
        high = len(nums)

        while (low < high):
            mid = low + ((high - low) // 2)

            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                high = mid
            elif (nums[mid] < target):
                low = mid + 1

        return low


# init solution
sol = Solution()

nums = [-1, 3, 4, 5, 6]
target = 0

result = sol.searchInsert(nums, target)
print(result)

nums = [-1, 2, 3, 5, 6]
target = 4

result = sol.searchInsert(nums, target)
print(result)
