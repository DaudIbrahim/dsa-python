def recursiveFactorial(n):
    # Constraints
    assert n >= 0 and int(n) == n, 'The Number must be a positive integer only'

    # Base Case
    if n in [0, 1]:
        return 1
    # Recursive Case
    else:
        return n * recursiveFactorial(n-1)


print(recursiveFactorial(5))
