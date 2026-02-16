# flake8: noqa

"""
Test cases for array_reverse_in_place implementation.
Tests both two-pointers and index-mirroring approaches.
"""

from array_reverse_in_place import reverse_in_place_two_pointers, reverse_in_place_index_mirroring


class TestReverseInPlaceTwoPointers:
    """Test suite for two pointers approach"""

    def test_reverses_odd_length_array(self):
        """Should reverse array with odd number of elements"""
        arr = [1, 2, 3, 4, 5]
        result = reverse_in_place_two_pointers(arr)
        assert result == [5, 4, 3, 2, 1]
        assert arr == [5, 4, 3, 2, 1]  # Verify in-place modification

    def test_reverses_even_length_array(self):
        """Should reverse array with even number of elements"""
        arr = [1, 2, 3, 4]
        result = reverse_in_place_two_pointers(arr)
        assert result == [4, 3, 2, 1]
        assert arr == [4, 3, 2, 1]

    def test_single_element(self):
        """Should handle single element array"""
        arr = [42]
        result = reverse_in_place_two_pointers(arr)
        assert result == [42]
        assert arr == [42]

    def test_two_elements(self):
        """Should reverse two element array"""
        arr = [1, 2]
        result = reverse_in_place_two_pointers(arr)
        assert result == [2, 1]
        assert arr == [2, 1]

    def test_empty_array(self):
        """Should handle empty array"""
        arr = []
        result = reverse_in_place_two_pointers(arr)
        assert result == []
        assert arr == []

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-1, -2, -3, -4, -5]
        result = reverse_in_place_two_pointers(arr)
        assert result == [-5, -4, -3, -2, -1]

    def test_mixed_positive_negative(self):
        """Should work with mixed positive and negative numbers"""
        arr = [-2, -1, 0, 1, 2]
        result = reverse_in_place_two_pointers(arr)
        assert result == [2, 1, 0, -1, -2]

    def test_duplicate_elements(self):
        """Should handle arrays with duplicate elements"""
        arr = [1, 2, 2, 3, 3, 3]
        result = reverse_in_place_two_pointers(arr)
        assert result == [3, 3, 3, 2, 2, 1]

    def test_large_array(self):
        """Should work with larger arrays"""
        arr = list(range(1, 101))  # [1, 2, 3, ..., 100]
        result = reverse_in_place_two_pointers(arr)
        assert result == list(range(100, 0, -1))  # [100, 99, 98, ..., 1]

    def test_all_same_elements(self):
        """Should handle array with all same elements"""
        arr = [5, 5, 5, 5, 5]
        result = reverse_in_place_two_pointers(arr)
        assert result == [5, 5, 5, 5, 5]


class TestReverseInPlaceIndexMirroring:
    """Test suite for index mirroring approach"""

    def test_reverses_odd_length_array(self):
        """Should reverse array with odd number of elements"""
        arr = [1, 2, 3, 4, 5]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [5, 4, 3, 2, 1]
        assert arr == [5, 4, 3, 2, 1]  # Verify in-place modification

    def test_reverses_even_length_array(self):
        """Should reverse array with even number of elements"""
        arr = [1, 2, 3, 4]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [4, 3, 2, 1]
        assert arr == [4, 3, 2, 1]

    def test_single_element(self):
        """Should handle single element array"""
        arr = [42]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [42]
        assert arr == [42]

    def test_two_elements(self):
        """Should reverse two element array"""
        arr = [1, 2]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [2, 1]
        assert arr == [2, 1]

    def test_empty_array(self):
        """Should handle empty array"""
        arr = []
        result = reverse_in_place_index_mirroring(arr)
        assert result == []
        assert arr == []

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-1, -2, -3, -4, -5]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [-5, -4, -3, -2, -1]

    def test_mixed_positive_negative(self):
        """Should work with mixed positive and negative numbers"""
        arr = [-2, -1, 0, 1, 2]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [2, 1, 0, -1, -2]

    def test_duplicate_elements(self):
        """Should handle arrays with duplicate elements"""
        arr = [1, 2, 2, 3, 3, 3]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [3, 3, 3, 2, 2, 1]

    def test_large_array(self):
        """Should work with larger arrays"""
        arr = list(range(1, 101))  # [1, 2, 3, ..., 100]
        result = reverse_in_place_index_mirroring(arr)
        assert result == list(range(100, 0, -1))  # [100, 99, 98, ..., 1]

    def test_all_same_elements(self):
        """Should handle array with all same elements"""
        arr = [5, 5, 5, 5, 5]
        result = reverse_in_place_index_mirroring(arr)
        assert result == [5, 5, 5, 5, 5]


class TestBothApproachesEquivalence:
    """Test that both approaches produce identical results"""

    def test_both_approaches_same_result_odd(self):
        """Both approaches should produce same result for odd length array"""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]

        result1 = reverse_in_place_two_pointers(arr1)
        result2 = reverse_in_place_index_mirroring(arr2)

        assert result1 == result2

    def test_both_approaches_same_result_even(self):
        """Both approaches should produce same result for even length array"""
        arr1 = [1, 2, 3, 4, 5, 6]
        arr2 = [1, 2, 3, 4, 5, 6]

        result1 = reverse_in_place_two_pointers(arr1)
        result2 = reverse_in_place_index_mirroring(arr2)

        assert result1 == result2

    def test_both_approaches_same_result_large(self):
        """Both approaches should produce same result for large array"""
        arr1 = list(range(1, 1001))
        arr2 = list(range(1, 1001))

        result1 = reverse_in_place_two_pointers(arr1)
        result2 = reverse_in_place_index_mirroring(arr2)

        assert result1 == result2
