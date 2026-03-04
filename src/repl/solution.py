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

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left_index = 0
        current_sum = 0
        best_length = float("inf")

        for right_index in range(0, len(nums)):
            current_sum += nums[right_index]

            while (current_sum >= target):
                best_length = min(
                    best_length, ((right_index - left_index) + 1))
                current_sum -= nums[left_index]
                left_index += 1

        if (best_length == float("inf")):
            return 0
        else:
            return best_length


# init solution
sol = Solution()

# run
nums = [3, 3, 4, 3, 0]
k = 3
# Output: 3.33333
print("\n", sol.findMaxAverage(nums, k))
