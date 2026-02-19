class Solution:
    def isPalindrome(self, s: str) -> bool:

        arr = []

        for character in s:
            if (character.isalnum()):
                arr.append(character.lower())

        filter_str = "".join(arr)

        # two pointers
        left = 0
        right = len(filter_str)

        while (left < right):

            if (filter_str[left] != filter_str[right - 1]):
                return False

            left += 1
            right -= 1

        return True


# init solution
sol = Solution()

# run
print(sol.isPalindrome("0P"))
