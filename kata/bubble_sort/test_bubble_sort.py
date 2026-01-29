"""
Test cases for bubble_sort implementation.
These tests follow the same pattern as Jest tests in JavaScript.
"""

from bubble_sort import bubble_sort


class TestBubbleSort:
    """Test suite for bubble sort algorithm"""

    def test_sorts_unsorted_array(self):
        """Should sort an unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert bubble_sort(arr) == expected

    def test_already_sorted_array(self):
        """Should handle already sorted array"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == expected

    def test_reverse_sorted_array(self):
        """Should sort reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == expected

    def test_empty_array(self):
        """Should return empty array for empty input"""
        arr = []
        assert bubble_sort(arr) == []

    def test_single_element(self):
        """Should handle single element array"""
        arr = [42]
        assert bubble_sort(arr) == [42]

    def test_two_elements_unsorted(self):
        """Should sort two element array"""
        arr = [2, 1]
        expected = [1, 2]
        assert bubble_sort(arr) == expected

    def test_two_elements_sorted(self):
        """Should handle two element sorted array"""
        arr = [1, 2]
        expected = [1, 2]
        assert bubble_sort(arr) == expected

    def test_duplicate_elements(self):
        """Should handle arrays with duplicate values"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
        assert bubble_sort(arr) == expected

    def test_all_same_elements(self):
        """Should handle array with all identical elements"""
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        assert bubble_sort(arr) == expected

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-5, 3, -1, 7, -10, 0]
        expected = [-10, -5, -1, 0, 3, 7]
        assert bubble_sort(arr) == expected

    def test_large_array(self):
        """Should work with larger arrays"""
        arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77]
        expected = [11, 12, 18, 22, 23, 25, 34, 36, 45, 50, 64, 77, 88, 90]
        assert bubble_sort(arr) == expected

    def test_does_not_modify_original(self):
        """Should not modify the original array"""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()
        bubble_sort(arr)
        assert arr == original
