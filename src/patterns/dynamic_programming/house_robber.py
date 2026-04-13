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

        # edge case: only one house, no choice to make
        if len(nums) == 1:
            return nums[0]

        # state: dp[i] = max loot from houses 0..i
        dp = [0] * len(nums)

        # base cases: smallest subproblems solved directly
        dp[0] = nums[0]  # one house — take it
        dp[1] = max(nums[0], nums[1])  # two houses — take the bigger

        # order: left → right, dependencies always ready
        for i in range(2, len(nums)):
            rob_i = nums[i] + dp[i - 2]  # decision: rob house i, skip i-1
            skip_i = dp[i - 1]  # decision: skip house i
            dp[i] = max(rob_i, skip_i)  # transition: best of both choices

        # last cell holds the answer for all n houses
        return dp[-1]


# ---------------------------------------------------------------

sol = Solution()
nums = [2, 7, 9, 3, 1]
print(sol.rob(nums))  # expected: 12
