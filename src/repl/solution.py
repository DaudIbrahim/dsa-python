class Solution:

    def findMaxAverage(self, nums: list[int], k: int) -> float:

        current_sum = 0
        window_avg = float("-inf")

        for right in range(0, len(nums)):

            current_sum += nums[right]

            if (right >= (k - 1)):
                current_avg = (current_sum / k)
                window_avg = max(current_avg, window_avg)
                current_sum -= nums[right - (k - 1)]

        return window_avg


# init solution
sol = Solution()

# run
nums = [3, 3, 4, 3, 0]
k = 3
# Output: 3.33333
print("\n", sol.findMaxAverage(nums, k))
