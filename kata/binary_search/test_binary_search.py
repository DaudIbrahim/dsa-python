"""
Test cases for binary_search implementation.
These tests follow the same pattern as Jest tests in JavaScript.
"""

from binary_search import binary_search


class TestBinarySearch:
    """Test suite for binary search algorithm"""

    def test_finds_element_in_middle(self):
        """Should find element in the middle of array"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 3) == 2

    def test_finds_first_element(self):
        """Should find element at the beginning"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 1) == 0

    def test_finds_last_element(self):
        """Should find element at the end"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 5) == 4

    def test_element_not_found(self):
        """Should return -1 when element is not in array"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 6) == -1

    def test_empty_array(self):
        """Should return -1 for empty array"""
        arr = []
        assert binary_search(arr, 1) == -1

    def test_single_element_found(self):
        """Should find element in single-element array"""
        arr = [42]
        assert binary_search(arr, 42) == 0

    def test_single_element_not_found(self):
        """Should return -1 when element not in single-element array"""
        arr = [42]
        assert binary_search(arr, 1) == -1

    def test_large_array(self):
        """Should work with larger arrays"""
        arr = list(range(0, 1000, 2))  # [0, 2, 4, 6, ..., 998]
        assert binary_search(arr, 500) == 250
        assert binary_search(arr, 999) == -1  # odd number, not in array

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-10, -5, 0, 5, 10]
        assert binary_search(arr, -5) == 1
        assert binary_search(arr, 0) == 2

    def test_duplicate_elements(self):
        """Should handle arrays with duplicates (returns any valid index)"""
        arr = [1, 2, 2, 2, 3]
        result = binary_search(arr, 2)
        # Should return one of the valid indices: 1, 2, or 3
        assert result in [1, 2, 3]
