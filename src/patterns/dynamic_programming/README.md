# Dynamic Programming

## DP Template

1. Define the subproblem
2. Identify base cases
3. Write the recurrence: dp[n] = f(dp[n-1], dp[n-2], ...)
4. Choose top-down (memo dict) or bottom-up (dp array)

- _top-down_ → big to small, recursion + hash table
- _bottom-up_ → small to big, loop + array
