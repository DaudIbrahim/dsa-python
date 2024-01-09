
def calculate_factorial_recursive(n):

    # Assert Constraint
    # Assert statement allows you to write sanity checks in your code.
    # https://realpython.com/python-assert-statement/
    assert int(n) == n and n >= 0

    # The in keyword has two purposes:
    # Check if a value is present in a sequence (list, range, string etc.)
    # & used to iterate through a sequence in a for loop
    # https://www.w3schools.com/python/ref_keyword_in.asp
    if (n in [0, 1]):
        # Base Case. Initial Condition.
        return 1
    else:
        # Inductive Case. Recursive Case.
        return n * calculate_factorial_recursive(n - 1)


# There are two types of loops built into Python: for loops & while loops
# https://www.freecodecamp.org/news/python-do-while-loop-example/
def calculate_factorial_iterative(n):

    assert int(n) == n and n >= 0

    val = 1
    index = 1

    while (index <= n):
        val = val * index
        index += 1

    return val


#
num = 3
print(f'Recursive Factorial for {num} is {calculate_factorial_recursive(num)}')
print(f'Iterative Factorial for {num} is {calculate_factorial_iterative(num)}')
