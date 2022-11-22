# Dynamic Fibonacci - https://youtu.be/vYquumk4nWw?t=142

def fibonacci(n):
    # Constraints
    assert n >= 0 and int(n) == n, 'The Number must be a positive integer only'

    # Base Case
    if n in [0, 1]:
        return 1
    # Recursive Case
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
