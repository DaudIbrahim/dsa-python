class Solution:
    def rob(self, nums: list[int]) -> int:

        # edge case
        if len(nums) == 1:
            return nums[0]

        # construct
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


# init solution
sol = Solution()

# run
nums = [2, 7, 9, 3, 1]


# Output
print("\n", sol.rob(nums))
