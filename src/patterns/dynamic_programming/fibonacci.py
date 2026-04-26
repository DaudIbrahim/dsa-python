# flake8: noqa

from functools import cache

# Top-Down DP vs Bottom-Up DP
# The core philosophical difference:
# Bottom-up says: "Let me build every answer from the ground up, smallest first, until I reach what I need."
# Top-down says: "I need fib(5). Let me just... ask for it. And figure out sub-problems only when I actually need them."
# With bottom-up, you proactively fill dp[0], dp[1], dp[2]... all the way up, even if you don't need some of them.
# With top-down, you're lazy — you only compute a value the first time someone asks for it.

# For example, Fibonacci series 10 terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21,
# 0th term -> 0
# 1st term -> 1
# 2nd term -> 1

# ---------------------------------------------------------------


# bottom-up DP (tabulation) (smallest → largest)
def fib_bottom_up(n):

    if n <= 0:
        return 0

    # dp_array[i] = term at i, derived from previous 0...(i-1)
    dp_array = []
    for i in range(0, n + 1):
        dp_array.append(0)

    # base case
    dp_array[0] = 0
    dp_array[1] = 1

    for i in range(2, n + 1):
        dp_array[i] = dp_array[i - 2] + dp_array[i - 1]

    return dp_array[n]


print(fib_bottom_up(40))

# ---------------------------------------------------------------


# top-down DP (memoization) (big → small)
dp_memoization_dict = dict()


def fib_number_top_down(n):
    if n in dp_memoization_dict:
        return dp_memoization_dict.get(n)
    if n <= 0:
        return 0
    if n == 1:
        return 1

    value = fib_number_top_down(n - 1) + fib_number_top_down(n - 2)
    dp_memoization_dict[n] = value
    return value


print(fib_number_top_down(40))

# ---------------------------------------------------------------


@cache
def fib_number_top_down_using_cache_decorator(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib_number_top_down_using_cache_decorator(
        n - 1
    ) + fib_number_top_down_using_cache_decorator(n - 2)


print(fib_number_top_down_using_cache_decorator(40))
