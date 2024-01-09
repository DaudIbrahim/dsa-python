# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci(n):

    # Assert Constraint
    # Not allowed to call: fibonacci(-1) OR fibonacci(4.5)
    assert int(n) == n and n >= 0, 'Fibonacci must be a positive integer'

    # Base Case. Initial Condition.
    if n in [0, 1]:
        return n
    else:
        # Inductive Case.
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(8))

n = int(input('Enter a number, N, N>=2 : '))
print(fibonacci(n))
