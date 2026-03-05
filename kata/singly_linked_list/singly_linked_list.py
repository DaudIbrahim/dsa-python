# flake8: noqa

class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, value: int):
        self.value: int = value
        self.next: "Node | None" = None


class SinglyLinkedList:
    """
    A singly linked list implementation.

    Each node holds a value and a reference to the next node.
    The list tracks its head node and its current size.
    """

    def __init__(self):
        self.head: Node | None = None
        self._size: int = 0

    # ------------------------------------------------------------------ #
    # Private
    # ------------------------------------------------------------------ #
    def _get_node_by_index(self, index: int) -> tuple[Node | None, Node | None]:

        # out of range
        if (index < 0 or index > self._size):
            raise IndexError("index out of range")

        # head
        if (index == 0):
            return [None, self.head]

        # >= 1
        i = 1
        prev_node = self.head
        node_at_idx = self.head.next

        while (node_at_idx):
            if (i == index):
                return [prev_node, node_at_idx]

            i += 1
            prev_node = node_at_idx
            node_at_idx = node_at_idx.next

        return [None, None]

    # ------------------------------------------------------------------ #
    # Insertion
    # ------------------------------------------------------------------ #
    def append(self, value: int) -> None:
        """Add a new node with *value* at the tail (end) of the list."""
        if (self.head is None):
            self.head = Node(value)
            self._size = 1
        else:
            insert_node = Node(value)
            prev_node, node_at_idx = self._get_node_by_index(self._size - 1)
            node_at_idx.next = insert_node
            self._size += 1

    def prepend(self, value: int) -> None:
        """Add a new node with *value* at the head (beginning) of the list."""
        if (self.head is None):
            self.head = Node(value)
            self._size = 1
        else:
            insert_node = Node(value)
            prev_node, node_at_idx = self._get_node_by_index(0)
            insert_node.next = node_at_idx
            self.head = insert_node
            self._size += 1

    def insert_at(self, index: int, value: int) -> None:
        """
        Insert a new node with *value* at the given *index*.

        Raises IndexError if index is out of range [0, size].
        """

        # out of range
        if (index < 0 or index > self._size):
            raise IndexError("index out of range")

        # start and end
        if (index == 0):
            self.prepend(value)
            return
        elif (index == (self._size)):
            self.append(value)
            return

        # in between
        insert_node = Node(value)
        prev_node, node_at_idx = self._get_node_by_index(index)
        prev_node.next = insert_node
        insert_node.next = node_at_idx
        self._size += 1

    # ------------------------------------------------------------------ #
    # Deletion
    # ------------------------------------------------------------------ #

    # TODO LinkedList Deletion
    def delete(self, value: int) -> bool:
        """
        Remove the first node whose value equals *value*.

        Returns True if a node was removed, False if *value* was not found.
        """
        pass

    def delete_at(self, index: int) -> int:
        """
        Remove and return the value of the node at *index*.

        Raises IndexError if index is out of range.
        """
        pass

    def delete_head(self) -> int:
        """
        Remove and return the value of the head node.

        Raises IndexError if the list is empty.
        """
        pass

    def delete_tail(self) -> int:
        """
        Remove and return the value of the tail node.

        Raises IndexError if the list is empty.
        """
        pass

    # ------------------------------------------------------------------ #
    # Access / Search
    # ------------------------------------------------------------------ #

    def get(self, index: int) -> int:
        """
        Return the value of the node at *index*.

        Raises IndexError if index is out of range.
        """
        pass

    def search(self, value: int) -> int:
        """
        Return the index of the first node whose value equals *value*.

        Returns -1 if *value* is not found.
        """
        pass

    def contains(self, value: int) -> bool:
        """Return True if any node holds *value*, False otherwise."""
        pass

    # ------------------------------------------------------------------ #
    # Properties / Utility
    # ------------------------------------------------------------------ #

    def size(self) -> int:
        """Return the number of nodes in the list."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the list has no nodes."""
        return self._size == 0

    def reverse(self) -> None:
        """Reverse the list in-place."""
        pass

    def to_list(self) -> list[int]:
        """Return a Python list containing all node values in order."""

        arr = []

        if (self.head):
            node = self.head
            while (node):
                arr.append(node.value)
                node = node.next

        return arr

    # ------------------------------------------------------------------ #
    # Magic methods (dunder methods)
    # ------------------------------------------------------------------ #

    def __len__(self) -> int:
        """Support len(linked_list)."""
        return self._size

    def __repr__(self) -> str:
        """Return a readable string representation, e.g. '1 -> 2 -> 3 -> None'."""
        pass
