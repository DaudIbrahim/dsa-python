# https://leetcode.com/problems/house-robber/description/

"""
House Robber — Bottom-up DP

  state:      dp[i] = max loot achievable from houses 0..i
  base cases: dp[0] = nums[0]  |  dp[1] = max(nums[0], nums[1])
  decision:   at each house — rob it or skip it
  transition: dp[i] = max(nums[i] + dp[i-2], dp[i-1])
  order:      left → right (dp[i] depends on dp[i-1] and dp[i-2])
"""


class Solution:
    def rob(self, nums: list[int]) -> int:

        # edge case
        if len(nums) == 1:
            return nums[0]

        # construct
        # dp[i] = max money robbing from houses 0..i
        dp = []
        for i in range(0, len(nums)):
            dp.append(0)

        # initial
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # now loot
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        # all houses checked
        return dp[-1]


# ---------------------------------------------------------------

sol = Solution()
nums = [2, 7, 9, 3, 1]
print(sol.rob(nums))  # expected: 12
