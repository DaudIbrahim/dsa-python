# flake8: noqa

"""
Test cases for prefix_sum implementation.
Tests both normal (index-aligned) and zero-offset (counting world) approaches.
"""

from prefix_sum import build_prefix_sum_normal, build_prefix_sum_zero_offset


class TestBuildPrefixSumNormal:
    """Test suite for normal (index-aligned) prefix sum"""

    def test_example_array(self):
        """Should compute prefix sums for [2, 5, 3, 7]"""
        arr = [2, 5, 3, 7]
        result = build_prefix_sum_normal(arr)
        assert result == [2, 7, 10, 17]

    def test_single_element(self):
        """Should handle single element array"""
        arr = [42]
        result = build_prefix_sum_normal(arr)
        assert result == [42]

    def test_two_elements(self):
        """Should compute prefix sums for two element array"""
        arr = [3, 4]
        result = build_prefix_sum_normal(arr)
        assert result == [3, 7]

    def test_empty_array(self):
        """Should handle empty array"""
        arr = []
        result = build_prefix_sum_normal(arr)
        assert result == []

    def test_all_zeros(self):
        """Should handle array of all zeros"""
        arr = [0, 0, 0, 0]
        result = build_prefix_sum_normal(arr)
        assert result == [0, 0, 0, 0]

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-1, -2, -3]
        result = build_prefix_sum_normal(arr)
        assert result == [-1, -3, -6]

    def test_mixed_positive_negative(self):
        """Should work with mixed positive and negative numbers"""
        arr = [3, -1, 4, -2]
        result = build_prefix_sum_normal(arr)
        assert result == [3, 2, 6, 4]

    def test_result_length_equals_input_length(self):
        """Result length should equal input length (length n)"""
        arr = [1, 2, 3, 4, 5]
        result = build_prefix_sum_normal(arr)
        assert len(result) == len(arr)

    def test_does_not_mutate_input(self):
        """Should not modify the original input array"""
        arr = [2, 5, 3, 7]
        original = arr[:]
        build_prefix_sum_normal(arr)
        assert arr == original


class TestBuildPrefixSumZeroOffset:
    """Test suite for zero-offset (counting world) prefix sum"""

    def test_example_array(self):
        """Should compute zero-offset prefix sums for [2, 5, 3, 7]"""
        arr = [2, 5, 3, 7]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, 2, 7, 10, 17]

    def test_first_element_always_zero(self):
        """P[0] should always be 0 — sum of zero elements"""
        arr = [2, 5, 3, 7]
        result = build_prefix_sum_zero_offset(arr)
        assert result[0] == 0

    def test_single_element(self):
        """Should handle single element array"""
        arr = [42]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, 42]

    def test_two_elements(self):
        """Should compute zero-offset prefix sums for two element array"""
        arr = [3, 4]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, 3, 7]

    def test_empty_array(self):
        """Should handle empty array — result is just [0]"""
        arr = []
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0]

    def test_all_zeros(self):
        """Should handle array of all zeros"""
        arr = [0, 0, 0, 0]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, 0, 0, 0, 0]

    def test_negative_numbers(self):
        """Should work with negative numbers"""
        arr = [-1, -2, -3]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, -1, -3, -6]

    def test_mixed_positive_negative(self):
        """Should work with mixed positive and negative numbers"""
        arr = [3, -1, 4, -2]
        result = build_prefix_sum_zero_offset(arr)
        assert result == [0, 3, 2, 6, 4]

    def test_result_length_equals_input_length_plus_one(self):
        """Result length should equal input length + 1 (length n+1)"""
        arr = [1, 2, 3, 4, 5]
        result = build_prefix_sum_zero_offset(arr)
        assert len(result) == len(arr) + 1

    def test_does_not_mutate_input(self):
        """Should not modify the original input array"""
        arr = [2, 5, 3, 7]
        original = arr[:]
        build_prefix_sum_zero_offset(arr)
        assert arr == original


class TestBothApproachesEquivalence:
    """Test that both approaches encode the same cumulative totals"""

    def test_last_element_equals_total_sum(self):
        """Both should end with the total sum of the array"""
        arr = [2, 5, 3, 7]
        normal = build_prefix_sum_normal(arr)
        zero_offset = build_prefix_sum_zero_offset(arr)

        assert normal[-1] == zero_offset[-1] == sum(arr)

    def test_zero_offset_is_normal_shifted_right_by_one(self):
        """
        Zero-offset P[i] == normal prefix[i-1] for i in 1..n
        P[0] = 0 (the sentinel that normal doesn't have)
        """
        arr = [2, 5, 3, 7]
        normal = build_prefix_sum_normal(arr)
        zero_offset = build_prefix_sum_zero_offset(arr)

        # P[1] == normal[0], P[2] == normal[1], etc.
        for i in range(len(arr)):
            assert zero_offset[i + 1] == normal[i]

    def test_equivalence_for_large_array(self):
        """Both approaches should agree on cumulative totals for larger arrays"""
        arr = list(range(1, 11))  # [1, 2, 3, ..., 10]
        normal = build_prefix_sum_normal(arr)
        zero_offset = build_prefix_sum_zero_offset(arr)

        assert normal[-1] == zero_offset[-1] == 55  # sum 1..10
