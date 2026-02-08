from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx1 = m - 1
        idx2 = n - 1
        insert_index = (m + n) - 1

        while (idx1 >= 0 and idx2 >= 0):

            if (nums2[idx2] >= nums1[idx1]):
                nums1[insert_index] = nums2[idx2]
                insert_index -= 1
                idx2 -= 1
            else:
                nums1[insert_index] = nums1[idx1]
                insert_index -= 1
                idx1 -= 1

        if (idx2 >= 0):
            for i in range(idx2, -1, -1):
                nums1[insert_index] = nums2[i]
                insert_index -= 1


# init solution
sol = Solution()


# 2. Define real arguments


# Input: nums1 = [1,2,3,0,0,0], idx1 = 3, nums2 = [2,5,6], idx2 = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1 = [1, 2, 3, 0, 0, 0]
idx1 = 3
nums2 = [2, 5, 6]
idx2 = 3

# 3. Run and Print
sol = Solution()
sol.merge(nums1, idx1, nums2, idx2)
print(nums1)
