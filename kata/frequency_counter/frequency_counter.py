"""
LeetCode 1: Character Frequency Counter

Given a string s, return a dictionary where each key is a character from the string
and each value is the number of times that character appears in the string.

Example 1:
Input: s = "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Example 2:
Input: s = "aabbcc"
Output: {'a': 2, 'b': 2, 'c': 2}

Example 3:
Input: s = ""
Output: {}

Constraints:
- 0 <= s.length <= 1000
- s consists of lowercase English letters

Topics: Hash Table, String
Difficulty: Easy
"""


class Solution:
    def frequencyCounter(self, s: str) -> dict:
        """
        Hash Map Approach - Frequency Counter Pattern

        Time Complexity: O(n) - Single pass through the string
        Space Complexity: O(k) - where k is the number of unique characters
        """
        hash_map = dict()

        for character in s:
            hash_map[character] = hash_map.get(character, 0) + 1

        return hash_map
