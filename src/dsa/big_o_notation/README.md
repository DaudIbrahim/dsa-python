# Big O Notation

## Overview

[neetcode big-o-notation](https://neetcode.io/courses/lessons/big-o-notation)

[Big O tells you how it an algorithm scales with respect to its input size](https://www.youtube.com/watch?v=7VHG6Y2QmtM&lc=UgwAxy3T3INAexROKJR4AaABAg)

[Big O Cheat Sheet](https://www.bigocheatsheet.com/)

- [Important concepts](https://theprimeagen.github.io/fem-algos/lessons/algorithms-and-time-space-complexity/time-and-space-complexity)

  - Growth is with respect to the input
  - Constants are dropped
  - Worst case is usually the way we measure

- Cases

  - Best Case - Big Omega
  - Average Case - Big Theta
  - Worst Case - Big O

## Read

Math

- Sets
- Functions
- [Introduction to Logarithms (1 of 2: Definition)](https://youtu.be/ntBWrcbAhaY)
  - [Anything to the power zero is ?](https://youtu.be/ntBWrcbAhaY?t=180)
- Big O Notation

## Common Time Complexities

| Big O             | Name             | Description                                                             |
| ----------------- | ---------------- | ----------------------------------------------------------------------- |
| \( O(1) \)        | Constant Time    | Execution time does not depend on input size.                           |
| \( O(\log n) \)   | Logarithmic Time | Execution time grows logarithmically with input size.                   |
| \( O(n) \)        | Linear Time      | Execution time grows linearly with input size.                          |
| \( O(n \log n) \) | Log-Linear Time  | Common in efficient sorting algorithms (e.g., Merge Sort, Quick Sort).  |
| \( O(n^2) \)      | Quadratic Time   | Nested loops; time grows quadratically with input size.                 |
| \( O(2^n) \)      | Exponential Time | Time doubles with each additional input (e.g., recursive Fibonacci).    |
| \( O(n!) \)       | Factorial Time   | Extremely inefficient; permutations of data (e.g., Traveling Salesman). |
