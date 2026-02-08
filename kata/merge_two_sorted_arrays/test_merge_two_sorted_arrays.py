"""
Test cases for merge_two_sorted_arrays implementation.
These tests follow the same pattern as Jest tests in JavaScript.
"""

from merge_two_sorted_arrays import merge_two_sorted_arrays


class TestMergeTwoSortedArrays:
    """Test suite for merging two sorted arrays"""

    def test_merges_two_sorted_arrays(self):
        """Should merge two sorted arrays into one sorted array"""
        arr_one = [1, 3, 5, 7]
        arr_two = [2, 4, 6, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_first_array_smaller(self):
        """Should handle when first array is smaller"""
        arr_one = [1, 2]
        arr_two = [3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_second_array_smaller(self):
        """Should handle when second array is smaller"""
        arr_one = [1, 2, 3, 4, 5]
        arr_two = [6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_first_array_empty(self):
        """Should handle empty first array"""
        arr_one = []
        arr_two = [1, 2, 3]
        expected = [1, 2, 3]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_second_array_empty(self):
        """Should handle empty second array"""
        arr_one = [1, 2, 3]
        arr_two = []
        expected = [1, 2, 3]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_both_arrays_empty(self):
        """Should return empty array when both inputs are empty"""
        arr_one = []
        arr_two = []
        assert merge_two_sorted_arrays(arr_one, arr_two) == []

    def test_single_element_arrays(self):
        """Should merge two single-element arrays"""
        arr_one = [1]
        arr_two = [2]
        expected = [1, 2]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_overlapping_ranges(self):
        """Should handle arrays with overlapping value ranges"""
        arr_one = [1, 5, 9, 13]
        arr_two = [2, 6, 10, 14]
        expected = [1, 2, 5, 6, 9, 10, 13, 14]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_duplicate_values_across_arrays(self):
        """Should handle duplicate values across both arrays"""
        arr_one = [1, 3, 5, 7]
        arr_two = [3, 5, 7, 9]
        expected = [1, 3, 3, 5, 5, 7, 7, 9]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_all_duplicates(self):
        """Should handle arrays with all identical elements"""
        arr_one = [5, 5, 5]
        arr_two = [5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5, 5, 5]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr_one = [-10, -5, 0, 5]
        arr_two = [-8, -3, 2, 7]
        expected = [-10, -8, -5, -3, 0, 2, 5, 7]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_all_negative_numbers(self):
        """Should work with all negative numbers"""
        arr_one = [-20, -15, -10]
        arr_two = [-18, -12, -5]
        expected = [-20, -18, -15, -12, -10, -5]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_first_array_all_smaller(self):
        """Should handle when all elements in first array are smaller"""
        arr_one = [1, 2, 3]
        arr_two = [10, 20, 30]
        expected = [1, 2, 3, 10, 20, 30]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_second_array_all_smaller(self):
        """Should handle when all elements in second array are smaller"""
        arr_one = [10, 20, 30]
        arr_two = [1, 2, 3]
        expected = [1, 2, 3, 10, 20, 30]
        assert merge_two_sorted_arrays(arr_one, arr_two) == expected

    def test_does_not_modify_originals(self):
        """Should not modify the original arrays"""
        arr_one = [1, 3, 5]
        arr_two = [2, 4, 6]
        original_one = arr_one.copy()
        original_two = arr_two.copy()
        merge_two_sorted_arrays(arr_one, arr_two)
        assert arr_one == original_one
        assert arr_two == original_two
