# Draft

The Last Algorithms Course You'll Need from frontendmasters by ThePrimeagen
and just summarize what are the data strcuture and algorithms he teaches

## Condensed Tracker — The Last Algorithms Course You'll Need

### Foundations

- Big-O notation
- Time complexity analysis
- Space complexity analysis

### Arrays

- Array fundamentals
- Array operations & complexity

### Searching

- Linear Search
- Binary Search
- Two Crystal Balls problem

### Sorting

- Bubble Sort
- Quick Sort
- Quick Sort partitioning

### Recursion

- Recursion fundamentals
- Recursive problem solving

### Linked Lists

- Singly Linked List
- Doubly Linked List

### Stack

- Stack data structure
- Push / Pop operations

### Queue

- Queue data structure
- Enqueue / Dequeue operations

### Trees

- Binary Tree fundamentals
- Tree traversal: Preorder
- Tree traversal: Inorder
- Tree traversal: Postorder

### Tree Searching

- Depth-First Search (DFS)
- Breadth-First Search (BFS)

### Heap

- Binary Heap
- Priority Queue

### Graphs

- Graph fundamentals
- Adjacency List representation
- Adjacency Matrix representation
- Graph DFS
- Graph BFS

### Pathfinding

- Dijkstra’s shortest path algorithm

### Hashing

- Hash maps
- Hashing basics
- Collision handling

### System Design Example

- LRU Cache (HashMap + Doubly Linked List)

✔ If you want, I can also show you something **very useful Prime actually hints at but doesn't explicitly list**:

**The 10 core algorithms that generate ~80% of interview questions.**

Most people miss this and end up studying way more DSA than needed.

---

Since you're preparing for **coding rounds**, the best order is based on **how often topics appear in interviews** and **how fast you can learn them**.

Right now you already know many **array-based patterns**, so you should add the remaining **core linear data structures first**, then move to heaps.

Here’s the most efficient order 👇

---

---

---

---

---

---

# Best Next Order AFTER BINARY SEARCH TREES

### 1️⃣ Linked Lists (Do this first)

Linked lists appear **very frequently** in coding rounds.

Focus on:

**Core operations**

- Reverse Linked List
- Detect Cycle (Floyd’s algorithm)
- Merge Two Sorted Lists
- Remove Nth Node From End
- Middle of Linked List (slow & fast pointer)

These problems also strengthen **two-pointer thinking**, which you're already learning.

Typical interview pattern:

```
fast = head
slow = head
```

---

### 2️⃣ Stack

Stacks are **extremely common** because they solve many tricky problems.

Important problems:

- Valid Parentheses
- Min Stack
- Next Greater Element
- Daily Temperatures
- Evaluate Reverse Polish Notation

Stacks introduce the **monotonic stack pattern**, which appears a lot in interviews.

---

### 3️⃣ Queue

Queues themselves are simple, but they become important for **BFS** later.

Focus on:

- Implement Queue
- Circular Queue (concept)
- Queue using stacks
- BFS-style thinking

But queues alone don't appear as often as stacks.

---

### 4️⃣ Heap / Priority Queue (After That)

Now move to heaps.

Heaps are used for **Top-K problems**.

Common patterns:

- Kth Largest Element
- Top K Frequent Elements
- Merge K Sorted Lists
- Find Median from Data Stream

Python already gives you:

```python
import heapq
```

So you mainly learn **how to use it**, not implement it from scratch.

---

# Final Recommended Order

For coding rounds:

```
Binary Trees
↓
Linked Lists
↓
Stack
↓
Queue
↓
Heap / Priority Queue
↓
Graphs
```

---

# Why Heaps Should Not Come First

Heaps are powerful but **less fundamental** than stacks and linked lists.

Interview frequency roughly:

```
Arrays / HashMap        ⭐⭐⭐⭐⭐
Trees                   ⭐⭐⭐⭐
Stack                   ⭐⭐⭐⭐
Linked List             ⭐⭐⭐⭐
Heap                    ⭐⭐⭐
Graph                   ⭐⭐⭐
Queue                   ⭐⭐
```

---

# Small Tip

Try learning **data structure + 3 problems**.

Example:

Linked List:

```
Reverse Linked List
Detect Cycle
Merge Two Sorted Lists
```

Stack:

```
Valid Parentheses
Daily Temperatures
Next Greater Element
```

This is **much more efficient than theory-heavy study**.

---

✅ **Short answer**

Do them in this order:

```
Binary Trees
Linked Lists
Stack
Queue
Heap
```

---

If you want, I can also show you **the 15 most important coding interview problems** that cover **almost all patterns** (this saves tons of time).
