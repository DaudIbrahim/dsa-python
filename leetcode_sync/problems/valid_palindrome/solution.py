class Solution:
    def isPalindrome(self, inputString: str) -> bool:
        start = 0
        end = len(inputString) - 1

        while start < end:
            while inputString[start].isalnum() is False:
                start += 1
                if start > len(inputString) - 1:
                    return True

            while inputString[end].isalnum() is False:
                end -= 1
                if end < 0:
                    return True

            if inputString[start].lower() != inputString[end].lower():
                return False

            start += 1
            end -= 1

        return True
