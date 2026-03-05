# flake8: noqa

"""
Test cases for SinglyLinkedList implementation.
These tests follow the same pattern as the other kata test files.
"""

import pytest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedListAppend:
    """Tests for append()"""

    def test_append_to_empty_list(self):
        """Appending to an empty list should set head to the new node."""
        ll = SinglyLinkedList()
        ll.append(1)
        assert ll.head.value == 1

    def test_append_multiple_values(self):
        """Appended values should appear in order."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_append_increases_size(self):
        """size() should increment with each append."""
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        assert ll.size() == 2


class TestSinglyLinkedListPrepend:
    """Tests for prepend()"""

    def test_prepend_to_empty_list(self):
        """Prepending to an empty list should set head to the new node."""
        ll = SinglyLinkedList()
        ll.prepend(1)
        assert ll.head.value == 1

    def test_prepend_becomes_new_head(self):
        """Prepended value should become the new head."""
        ll = SinglyLinkedList()
        ll.append(2)
        ll.prepend(1)
        assert ll.head.value == 1

    def test_prepend_multiple_values(self):
        """Multiple prepends should reverse insertion order."""
        ll = SinglyLinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        assert ll.to_list() == [1, 2, 3]


class TestSinglyLinkedListInsertAt:
    """Tests for insert_at()"""

    def test_insert_at_beginning(self):
        """Inserting at index 0 should behave like prepend."""
        ll = SinglyLinkedList()
        ll.append(2)
        ll.append(3)
        ll.insert_at(0, 1)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_end(self):
        """Inserting at the last valid index should behave like append."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.insert_at(2, 3)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_middle(self):
        """Inserting in the middle should shift subsequent nodes."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(3)
        ll.insert_at(1, 2)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_out_of_range_raises(self):
        """Inserting at an invalid index should raise IndexError."""
        ll = SinglyLinkedList()
        with pytest.raises(IndexError):
            ll.insert_at(5, 99)


# class TestSinglyLinkedListDelete:
#     """Tests for delete()"""

#     def test_delete_existing_value_returns_true(self):
#         """delete() should return True when a node is removed."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         assert ll.delete(1) is True

#     def test_delete_missing_value_returns_false(self):
#         """delete() should return False when value is not found."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         assert ll.delete(99) is False

#     def test_delete_head_node(self):
#         """Deleting the head should update head to the next node."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.delete(1)
#         assert ll.head.value == 2

#     def test_delete_tail_node(self):
#         """Deleting the tail should leave the rest of the list intact."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.append(3)
#         ll.delete(3)
#         assert ll.to_list() == [1, 2]

#     def test_delete_middle_node(self):
#         """Deleting a middle node should link its neighbours correctly."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.append(3)
#         ll.delete(2)
#         assert ll.to_list() == [1, 3]

#     def test_delete_only_first_occurrence(self):
#         """delete() should remove only the first occurrence of a duplicate value."""
#         ll = SinglyLinkedList()
#         ll.append(2)
#         ll.append(2)
#         ll.append(2)
#         ll.delete(2)
#         assert ll.size() == 2


# class TestSinglyLinkedListDeleteAt:
#     """Tests for delete_at()"""

#     def test_delete_at_head(self):
#         """delete_at(0) should remove and return the head value."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         assert ll.delete_at(0) == 1
#         assert ll.head.value == 2

#     def test_delete_at_tail(self):
#         """delete_at(last) should remove and return the tail value."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.append(3)
#         assert ll.delete_at(2) == 3
#         assert ll.to_list() == [1, 2]

#     def test_delete_at_middle(self):
#         """delete_at(mid) should remove the correct node."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.append(3)
#         assert ll.delete_at(1) == 2
#         assert ll.to_list() == [1, 3]

#     def test_delete_at_out_of_range_raises(self):
#         """delete_at() with an invalid index should raise IndexError."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         with pytest.raises(IndexError):
#             ll.delete_at(5)


# class TestSinglyLinkedListDeleteHeadTail:
#     """Tests for delete_head() and delete_tail()"""

#     def test_delete_head_returns_value(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         assert ll.delete_head() == 1

#     def test_delete_tail_returns_value(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         assert ll.delete_tail() == 2

#     def test_delete_head_on_empty_raises(self):
#         ll = SinglyLinkedList()
#         with pytest.raises(IndexError):
#             ll.delete_head()

#     def test_delete_tail_on_empty_raises(self):
#         ll = SinglyLinkedList()
#         with pytest.raises(IndexError):
#             ll.delete_tail()


# class TestSinglyLinkedListGet:
#     """Tests for get()"""

#     def test_get_first_element(self):
#         ll = SinglyLinkedList()
#         ll.append(10)
#         ll.append(20)
#         assert ll.get(0) == 10

#     def test_get_last_element(self):
#         ll = SinglyLinkedList()
#         ll.append(10)
#         ll.append(20)
#         assert ll.get(1) == 20

#     def test_get_out_of_range_raises(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         with pytest.raises(IndexError):
#             ll.get(5)


# class TestSinglyLinkedListSearch:
#     """Tests for search()"""

#     def test_search_existing_value(self):
#         """search() should return the index of the value."""
#         ll = SinglyLinkedList()
#         ll.append(10)
#         ll.append(20)
#         ll.append(30)
#         assert ll.search(20) == 1

#     def test_search_missing_value(self):
#         """search() should return -1 when not found."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         assert ll.search(99) == -1

#     def test_search_returns_first_occurrence(self):
#         """search() should return the index of the first match."""
#         ll = SinglyLinkedList()
#         ll.append(5)
#         ll.append(5)
#         assert ll.search(5) == 0


# class TestSinglyLinkedListContains:
#     """Tests for contains()"""

#     def test_contains_existing_value(self):
#         ll = SinglyLinkedList()
#         ll.append(7)
#         assert ll.contains(7) is True

#     def test_contains_missing_value(self):
#         ll = SinglyLinkedList()
#         ll.append(7)
#         assert ll.contains(99) is False

#     def test_contains_on_empty_list(self):
#         ll = SinglyLinkedList()
#         assert ll.contains(1) is False


# class TestSinglyLinkedListUtility:
#     """Tests for size(), is_empty(), __len__(), reverse(), to_list()"""

#     def test_size_empty_list(self):
#         assert SinglyLinkedList().size() == 0

#     def test_is_empty_on_new_list(self):
#         assert SinglyLinkedList().is_empty() is True

#     def test_is_empty_after_append(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         assert ll.is_empty() is False

#     def test_len_builtin(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         assert len(ll) == 2

#     def test_to_list_empty(self):
#         assert SinglyLinkedList().to_list() == []

#     def test_to_list_multiple(self):
#         ll = SinglyLinkedList()
#         for v in [1, 2, 3]:
#             ll.append(v)
#         assert ll.to_list() == [1, 2, 3]

#     def test_reverse_empty_list(self):
#         """Reversing an empty list should not raise."""
#         ll = SinglyLinkedList()
#         ll.reverse()
#         assert ll.to_list() == []

#     def test_reverse_single_element(self):
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.reverse()
#         assert ll.to_list() == [1]

#     def test_reverse_multiple_elements(self):
#         ll = SinglyLinkedList()
#         for v in [1, 2, 3, 4]:
#             ll.append(v)
#         ll.reverse()
#         assert ll.to_list() == [4, 3, 2, 1]

#     def test_repr_non_empty(self):
#         """__repr__ should return a human-readable arrow-linked string."""
#         ll = SinglyLinkedList()
#         ll.append(1)
#         ll.append(2)
#         ll.append(3)
#         assert repr(ll) == "1 -> 2 -> 3 -> None"
