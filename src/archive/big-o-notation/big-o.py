def multiply_number(n):
    # Big O - O(1)
    return n * n


def print_items(n):
    # Big O - O(N)
    # Drop Constants
    for i in range(n):
        print(i)


def print_items1(n):
    # Big O - O(n^2)
    # Drop Non Dominant Terms
    for i in range(n):  # O(N)
        for j in range(n):  # O(N)
            # n * n = n ^ 2
            print(n, j)

    # Big O - O(logN)
    # Divide & Conquer Approach. Example (Binary Search)
    # Space Complexity


def sum(n):
    # Space Complexity
    # Big O - O(N)
    if n <= 0:
        return 0
    return n + sum(n - 1)


def print_items2(a, b):
    # Space Complexity O(A + B)
    # Different Terms for Input - Add vs Multiply

    for i in range(a):  # O(a)
        print(i)

    for i in range(b):  # O(b)
        print(i)

    # O(a+b) |Add


def print_items3(a, b):
    # Space Complexity O(A + B)
    # Different Terms for Input - Add vs Multiply

    for i in range(a):  # O(a)
        print(i)

    for i in range(b):  # O(b)
        print(i)

    # O(a+b) | Add


def print_items4(a, b):
    # Space Complexity O(A * B)
    # Different Terms for Input - Add vs Multiply

    for i in range(a):  # O(a)
        for i in range(b):  # O(b)
            print(i)

    # O(a * b)
