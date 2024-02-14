from typing import List


# Define the Solution class
class Solution:
    def naive_two_sum_while(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1

        while i < len(nums):
            while j < len(nums):
                total = nums[i] + nums[j]
                if total == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1
        return []

    def naive_two_sum_for(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i, element_inner in enumerate(nums):
            sliceIdx = i + 1
            for j, element_outer in enumerate(nums[sliceIdx:], start=i + 1):
                if element_inner + element_outer == target:
                    result.append(i)
                    result.append(j)
                    return result
        return []


# Instantiate the Solution class
sol = Solution()

# Call the methods and print the results
result1 = sol.naive_two_sum_while([2, 7, 11, 15], 9)
result2 = sol.naive_two_sum_for([2, 7, 11, 15], 9)

print("Result from naive_two_sum_while:", result1)
print("Result from naive_two_sum_for:", result2)
