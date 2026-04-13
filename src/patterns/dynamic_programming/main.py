# from functools import cache
# @cache

# For example, Fibonacci series 10 terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21,


# memoization
memo = dict()


# top-down DP (memoization) (big → small)
def fib_number_top_down(n):

    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fib_number_top_down(n - 2) + fib_number_top_down(n - 1)
    return memo[n]


print(fib_number_top_down(40))


# bottom-up DP (tabulation) (smallest → largest)
def fib_bottom_up(n):
    if n <= 0:
        return 0

    # constrcut dp table
    dp = []
    for i in range(0, n + 1):
        dp.append(0)
    dp[0] = 0
    dp[1] = 1

    # compute for nth term
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


print(fib_bottom_up(40))
