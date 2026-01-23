"""
Test cases for Character Frequency Counter
Run with: pytest kata/frequency_counter/test_frequency_counter.py -v
"""

import pytest
from frequency_counter import Solution


class TestFrequencyCounter:
    
    def setup_method(self):
        """Initialize Solution instance before each test"""
        self.solution = Solution()
    
    def test_basic_string(self):
        """Test with basic string"""
        assert self.solution.frequencyCounter("hello") == {
            'h': 1, 'e': 1, 'l': 2, 'o': 1
        }
    
    def test_repeated_characters(self):
        """Test with repeated characters"""
        assert self.solution.frequencyCounter("aabbcc") == {
            'a': 2, 'b': 2, 'c': 2
        }
    
    def test_empty_string(self):
        """Test with empty string"""
        assert self.solution.frequencyCounter("") == {}
    
    def test_single_character(self):
        """Test with single character"""
        assert self.solution.frequencyCounter("a") == {'a': 1}
    
    def test_all_same_character(self):
        """Test with all same characters"""
        assert self.solution.frequencyCounter("aaaa") == {'a': 4}
    
    def test_unique_characters(self):
        """Test with all unique characters"""
        assert self.solution.frequencyCounter("abcdefg") == {
            'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1
        }
    
    def test_longer_string(self):
        """Test with longer string"""
        result = self.solution.frequencyCounter("programming")
        assert result['g'] == 2
        assert result['r'] == 2
        assert result['m'] == 2
        assert result['p'] == 1
