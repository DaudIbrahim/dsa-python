# [Two Pointers](https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days)

The Two Pointers pattern is a technique used in solving problems where you iterate through an array or a sequence using two pointers. The key idea is to have two pointers, usually initialized at different positions in the array, and then move them towards each other, or in some cases, in the same direction with a certain condition. This pattern is particularly useful for optimizing solutions with linear time complexity.

There are two main scenarios where the Two Pointers pattern is often applied:

1. **Two Pointers Approach - Same Direction:**
   - In this scenario, both pointers start at the same end of the array (either at the beginning or at the end), and they move in the same direction.
   - The purpose is to efficiently search for a pair or a subarray that satisfies a certain condition.

2. **Two Pointers Approach - Opposite Direction:**
   - In this scenario, the two pointers start at opposite ends of the array, and they move towards each other.
   - The purpose is often to find a solution that meets certain conditions or constraints.

Common use cases for the Two Pointers pattern include:

- **Searching for a pair:** When you need to find two elements in an array that meet certain conditions.

- **Searching for a subarray or range:** When you need to find a subarray or range of elements that satisfies specific criteria.

  - Subarray - A subarray refers to a contiguous sequence of elements within an array. In simpler terms, it's a portion of an array where the elements are taken continuously in their original order. The subarray is defined by specifying the starting and ending indices within the array.

- **Checking for a palindrome:** When you need to determine whether a sequence (e.g., string or array) is a palindrome.

The Two Pointers pattern can be more efficient than naive approaches, such as nested loops, because it often reduces the time complexity from O(n^2) to O(n) or O(n log n).

Understanding this conceptually is crucial before diving into the code. It's about optimizing your solution by intelligently using two pointers to traverse the data in an organized manner, reducing the time complexity of the algorithm.

## [Two Pointers Leetcode](https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days)

1. Running from both ends of an array
2. Fast and Slow Pointers
3. Running from beginning of 2 arrays / Merging 2 arrays
4. Split & Merge of an array / Divide and Conquer
