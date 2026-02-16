from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_index = 0
        right_index = len(numbers) - 1

        while (left_index != right_index):
            sum = numbers[left_index] + numbers[right_index]

            if (target == sum):
                return [left_index + 1, right_index + 1]
            elif (target > sum):
                left_index += 1
            else:
                right_index -= 1

        return []


# init solution
sol = Solution()

# 2.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 3. Run
sol = Solution()
print(sol.twoSum([2, 3, 4], 6))
