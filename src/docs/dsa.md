# [Data Structures and Algorithms](https://youtube.com/playlist?list=PLxvbXPxg6ydxE3bOWlrAaMsRiY-kVNVGS&si=qtMPRLMM6KTnx56S)

*The goal of programming is to create solutions, not to type on a keyboard. Generating a solution that is both legitimate and machine-readable, and then effectively handing that solution, the set of instructions, to the computer to process. In essence, the machine runs the computation on your given solution, and you are responsible for checking the accuracy of your solution. I could go on about this indefinitely, but you get the idea. You create the solutions, and the computer computes them. This is when proofs enter the picture to demonstrate the correctness of a particular algorithmic formula.*

- Adopt the mindset of *Think First; Code Second*

- Grow a core competency in *Translating Abstraction into Concreteness*.  [It's definitely a core competency.If you can get really good at this visualizing creating your problems firston a whiteboard, and then being able to translate abstraction into concreteness.](https://frontendmasters.com/courses/algorithms/linear-search-kata-setup/?t=52)

- Visualizing: Creating your problems first on a whiteboard, and then being able to [translate abstraction into concreteness](https://github.com/DaudIbrahim/knowledge-base-pvt/blob/main/ideas-and-knowledge-the-power-beyond-the-tool.md).

  - [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

  - [VisuAlgo](https://visualgo.net/en)

## PSET

Problem Set

### Nature of the Scientific Process

Problem sets are great ways to provide students with the practice necessary to gain mastery of new skills that you have introduced in class. Problem sets are also great at reflecting the nature of the [scientific process](https://bokcenter.harvard.edu/problem-sets "Harvard University"), which so often involves problem solving, and in so doing help reinforce the explanatory power of your discipline.

### Problem Solving `Goal`

**[The Focus Time](https://www.youtube.com/watch?v=zvrleanEYOw&t=37s "Grant Sanderson") that you are spending should be on solving specific problems.**

**Try to push yourself to solve more problems than you naturally would.**

It is more important to be able to Recognize a problem, than to Memorize an algorithm that solves it. - [John Byrd](https://qr.ae/priZWZ)

- *Recogize-Learn* `Problems`
- *Identify* `Patterns`
- *Create* `Solutions`

#### [My approach to practice: problem solving](https://youtu.be/xF554Tlzo-c?t=309)

Spend [60 minutes](https://youtu.be/oUJlLAdQGIk?&t=77) of focus time on solving a problem

- You solved it - `Great`

  - You did'nt

    1. Spend the rest of you time learning the solution
    2. Re-Implement the Solution from scratch by yourself **Do It!**
    3. Consider checking the solution after an hour of effort on a problem is a reasonable approach. The key is not just in peeking but in thoroughly understanding the solution, learning the underlying concepts, and challenging yourself to reimplement it from scratch. The goal is not only to solve the problem but to deepen your understanding and enhance your problem-solving skills. *31-Jan-24*

## Strcuture & Elements & Operations

### Operations : Manipulating the Strcuture (Example Array)

- Create | Create the 2D Data Structure
- Traversal | Traverse the 2D Data Structure
- [Merge](https://www.adservio.fr/post/data-structure-types-operations)
- Copy

### Operations : Manipulating the Data (Example Elements in an Array)

[Big-O Cheat Sheet](https://www.bigocheatsheet.com/ 'bigocheatsheet')

- Access
- Search
- Insertion
- Deletion

## [Set Theory](https://youtu.be/5ZhNmKb-dqk?list=PLxvbXPxg6ydxE3bOWlrAaMsRiY-kVNVGS)

Cardinality of the Union and Intersection

[Cardinality](https://www.cuemath.com/algebra/cardinality/) refers to the number that is obtained after counting something. Thus, the cardinality of a set is the number of elements in it. For example, the set {1, 2, 3, 4, 5} has cardinality five which is more than the cardinality of {1, 2, 3} which is three.

An *identity* is an equation that is always true, no matter what values are substituted into it. Think of it as a rule or formula that holds universally. Identities are specific equations or statements that are universally true across all values of the variables involved.

*Axioms* -> *Identity*

Buildinog Blocks

- Axioms
- Definitions
- Theorems
- Proofs
- Identities
- Conjectures

Set *Compliments* negation

De Morgan's Law

Russel's Paradox

[Paradox of Self Reference](https://youtu.be/HeQX2HjkcNo?t=566)

The paradox considers the set R of all sets that do not contain themselves as members. The question then becomes: Does R contain itself?

1. If R contains itself, then by definition, it should not be in R (because R is the set of sets that do not contain themselves).

2. If R does not contain itself, then it meets the criteria for membership in R, so it should be in R.

*Example*: Imagine you're making a list of all the lists that don't include themselves. Let's call this list R.

Now, we ask a tricky question: Should R be on this list?

There are two possibilities:

1. If R is on the list, then it's a list that doesn't include itself. But wait, we just put it on the list, so that can't be right.

2. If R is not on the list, then it's a list that does include itself. But that means it should be on the list of lists that don't include themselves.

So we're stuck. If we put R on the list, it shouldn't be there. If we don't put R on the list, it should be there.

This is the paradox - no matter what we do, we end up contradicting ourselves. It's like a logical trap that shows there's a problem with how we're thinking about sets.

```python
# Python Set
# SQL Set
```

## Recursion

### Refer to the three key ideas that you have worked on before

1. Mathematical Induction
2. Recursive Leap of faith - Towers of Hanoi
3. Fibonacci Sequenct - Rcursion & Memoization

### Recursion Concepts

1. *Case*
    - Base Case
    - Inductive Case

2. *Function Properties. Every function has the following:*

    - Return Address - rA
    - Return Value- rV
    - Argument - A

    **Functions return: Sometimes you overlook this, in recursion we call functions recursively. Keep in mind the fact that a function always returns, regardless of whether it returns a void or a value. In a recursive manner you build up the stack with function call - you hit a base and the functions start to return, effectively emptying the call stack by popping of each function.**

3. *Recursion: Actions*

    - Pre - performing some Action before recursion
    - Recursion - the recursion call
    - Post - performing some Action after the recursion call

  Similar example you can think of traversing a tree by Pre-Order, In-Order, Post-Order

```js
// You're gonna really want to understand this. Is that recursion can actually be broken down or the recurse can actually be broke down into three steps, all right? So the recurse thing can be into three steps. You have a pre, which means you can do something before you recurse.

// In our case this was literally n+, right? We took n and we added it and then we did the recursion part. So this is kind of a pre thing. Now then, we recurse, which actually does the calling of the function, right? And then there's actually an availability for some sort of post operation.

// Does that make sort of sense? We can do something else after recursing. So we didn't actually have to return here, right? We don't have to return, we could have said, hey, out equals this, then console logged something, and then returned out, right? Which would have actually, let's say we console logged, ley's just say we, here I'll just break the word log.

// - [theprimeagen recursion](https://theprimeagen.github.io/fem-algos/lessons/recursion/recursion)
```

- [Pre Operation - Recursion - Post Operation Example in Code - MazeSolver](../kata-machine//src//day1/MazeSolver.ts)

## [Mathematical Induction & Recursion (Relationship)](https://stackoverflow.com/a/11143870/7031530 "stackoverflow")

### Sequence

You Start with a Sequence.

You identify a pattern that seems to hold true for every term in the Sequence.

Make use of Mathematical Induction to prove that the pattern holds true for every term down the Sequence.

### Method of Proof by Mathematical Induction

    - Step 1. Basis Step.
        Show that P(a) is true. Pattern that seems to hold true from a.

    - Step 2. Inductive Step
        For every integer k >= a
            If P(k) is true then P(k+1) is true.
                To perform this Inductive step you make the Inductive Hypothesis. (P(k) is true)
                Supposition: that P(k) is true, where k is any particular, but arbitrarily chosen integer with k >= a.
                Inductive Hypothesis is the supposition that P(k) is true
            Show that P(k + 1) is true
                Notice: a, a+1, a+2, a+3, ... k, k+1
                            for every integer k >= a, that p(k) is true

### Recursion (Mathematical)

    Start with Sequence: Each term has a recurrence relation with the previous term.

    A recurrence relation is an equation that defines each later terms of a Sequence by reference to earlier terms in the Sequence
            Now you have a Sequence at hand and for defining the nth term of the Sequence you refer (nth - 1), (nth -2) ...
    Initial Condition
        An Initial Term that is defined (returns a value)
            As previously mentioned for defining the nth term of the Sequence you refer (nth - 1), (nth -2) ... an so forth until reaching the initial term that starts solving the problem for defining the nth term of the Sequence
                Notice: n, n-1, n-2, n-3, ... Initial Term

### Recursive Specification

    Recursive Relation
    Initial Values

### Combine

    - Sequence.
    - Recursive Specification: Recurrence Ralation & Initial Condition.
    - Explicit Formula: Solution to the Recurrence Ralation.
    - Correctedness of the formula proven by Mathematical Induction.

### [Recursive Leap of Faith](https://www.youtube.com/watch?v=rf6uf3jNjbo&t=620s)

The most difficult part of solving problems recursively is to figure out how knowing the solution to the smaller problems of the same type as the orignal problem will give you a solution to the problem as a whole.

You suppose you know the solutions to the smaller subproblems, the supposition that the smaller subproblems have already been solved has been called the Recursive Leap of Faith.

The Recursive Leap of Faith is similar to the inductive hypothesis in a proof by mathematical induction.

### Relationship between Mathematical Induction & Recursion?

- Sequence

  - Think in terms of the following:

         Sequence, Pattern & Terms.

         Both Mathematical Induction & Recursion deal with these.

- Direction

  - Mathematical Induction

         `a, (a+1), (a+2), (a+3), ... k, (k+1)`

         Start from base term `a` and prove that for `k >= a`, every subsequent `k + 1` is true

  - Recursion

         `k, (k-1), (k-2), (k-3), ... k, a`

         Define the `kth term`.
         `k` refers to earlier terms in the sequence `(k-1)`, `(k-2)` preceding and so forth arriving at the initlal term `a`

    - Extra: Approx - ∞
      - Mathematical Induction: Base to ∞
      - Recursion ∞ to Initial Terms

- Supposition

  - Both Inductive Hypothesis & Recursive Leap of Faith deal with a Supposition; a Hypothesis.

        Mathematical Induction: Inductive Hypothesis is the supposition that P(k) is true; where k is any particular, but arbitrarily chosen integer with k >= a.
        Recursion: Recursive Leap of Faith is the supposition that the smaller subproblems have already been solved.

- Correctedness of the Explicit Formula proven by Mathematical Induction

    You use mathematical induction to check the correctness of your formula

#### Reference

- [Discrete Mathematics with Applications](https://www.amazon.com/dp/1337694193/ "Susanna S. Epp")

- [My Answer on stackoverflow](https://stackoverflow.com/a/75788144/7031530)

## Big O Notation

 **Big O Notation** - [Big O tells you how it an algorithm scales with respect to its input size](https://www.youtube.com/watch?v=7VHG6Y2QmtM&lc=UgwAxy3T3INAexROKJR4AaABAg)

[Big O Cheat Sheet](https://www.bigocheatsheet.com/)

- [Important concepts](https://theprimeagen.github.io/fem-algos/lessons/algorithms-and-time-space-complexity/time-and-space-complexity)
  - Growth is with respect to the input
  - Constants are dropped
  - Worst case is usually the way we measure

- Cases
  - Best Case - Big Omega
  - Average Case - Big Theta
  - Worst Case - Big O

- Reaading Material
  - [Big-O notation explained by a self-taught programmer](https://justin.abrah.ms/computer-science/big-o-notation-explained.html)

Math

- Sets
- Functions
- [Logarithms](https://youtu.be/ntBWrcbAhaY?t=180)
- Big O Notation

## Array

Random Access with an ArrayList. Example - Give me index three.

One key difference that with purely Arrays you essentually define a size aka a container

- In array operations `insert` and `write` mean two different things

  - Example An array of size 3. length of Three `[idx:0, idx:1, idx:2]`

    - At index 2 `write` value dummy-value. This is a write opration, writing at index 2

    - At index 3 `write` value duumy-data-2

      - Now observe that within an array with of capacity of three items you are writing data that exceeds the capacoty to 4 items

        - & behold the Array has to grow in size which is the `insert` operation

        - Ability to Grow

          - Create a new array with increased capacity
          - Copy existing items
          - Write the new item at index 4

In Python, Arrays are not a built-in language construct, and therefore need to be imported via the array module in order to be used.

### Dynamic Arrays

[What if you had to invent a dynamic array?](https://youtu.be/5AllG-i_yto)

### 2D Array

Graphs represented in an Adjacency Matrix are implemented in a 2D Array

- Implementation [Breadth First Search Graph Matrix](../kata-machine/src/day2/BFSGraphMatrix.ts)

### Linear Data Structures

[Structures can be broken down into two main categories, linear and nonlinear.](https://www.adservio.fr/post/data-structure-types-operations)

Main Linear Data Structures:

- Arrays

### Ueful Array Reference

- [1D Array using Python Module: Array](https://docs.python.org/3/library/array.html#module-array)

- [2D Arrays using Numpy](https://numpy.org/doc/stable/user/basics.creation.html)

- [Python Array vs List](https://learnpython.com/blog/python-array-vs-list/)

- [Python List VS Array VS Tuple](https://www.geeksforgeeks.org/python-list-vs-array-vs-tuple/)

Low level Array access = (a + width * offset)

## Python Lists

In Python, lists are implemented as dynamic arrays. The memory allocation for a dynamic array is different from that of a static array. When a dynamic array is created, it allocates a fixed amount of memory initially. As elements are added to the list, the dynamic array checks if it has enough capacity to store the new elements. If not, it reallocates a larger block of memory and copies the elements from the old block to the new one.

The size of the new block is typically a multiple of the old block's size (usually around 1.125 times, but this can vary depending on the implementation). This allows for amortized constant-time complexity for append operations.

When altering a dynamic array in Python, such as adding or removing elements, it does not always create a new array. If the current array has enough capacity to accommodate the changes, the operations are performed in-place without creating a new array.

However, if the dynamic array needs to be resized due to the change (either because it needs more capacity to store additional elements or because it can free up some memory by using a smaller block), a new array will be created, and the contents of the old array will be copied to the new one.

## Linked List

**Every single LinkedList is essentially a graph. Every single LinkedList is technically a tree.**

- Understand conceptually and implement with caution (easy to make mistake in implementation)

- Very Important as `Graphs and Trees` underneath use the very similar pointer mechanism of that of `Linked List`

### Singly Linked List

In a singly linked list, each node contains a data element and a reference (or link) to the next node in the sequence. Traversal can only be done in one direction, starting from the head and following the next pointers until reaching the tail. It is the simplest and most common type of linked list.

In a SinglyLinkedList we make use of offsetNode. (offsetNode - get the prev node to the current in order to update pointers). In comparison to doubly linked list we do not have pointers that point to previous node. Therefore for common operations such as delete node at index 4 you would need the offset node at index 3 and then update pointers acordingly.

### Doubly Linked List

In a doubly linked list, each node has references to both the next node and the previous node in the sequence. This allows for traversal in both forward and backward directions. The additional previous pointers provide more flexibility but require extra memory to store.

### Cyclic aka Circluar Linked List

Important to note when we say Circular then we are essentially reffering to the concept of `Cyclic!`

In this scenario nodes do not point to null in their terminating pointers instead they point back at the Linked List structure itself.

Nodes form a cycle rather than terminating with null pointers.

#### Singly Circular Linked List

A circular singly linked list is a linked list where the last node points back to the first node, forming a closed loop.

In a circular linked list, the tail node's next reference points back to the head, forming a loop. This means there is no end or null reference, and the list can be traversed indefinitely. Circular linked lists are useful in scenarios where cyclic behavior or continuous looping is required.

#### Doubly Circular Linked List

This type of linked list combines the features of a doubly linked list and a circular linked list. Each node has references to both the next and previous nodes, and the tail node's next reference points back to the head. This creates a circular loop that can be traversed in both directions.

### Linked List More

      Succeeding Node & Preceding node

## Stack

- *Stack - DFS - LIFO - ⬇*

## Queue

- *Queue - BFS - FIFO - ➡*

## Map/Dictionary

- Map/Dictionary

## Search

### [Binary Search](https://www.youtube.com/watch?v=KXJSjte_OAI&pp=ygUMYmlucmF5cyBlYXJj) *Paradigm of Divide and Conquer*

- [ThePrimeagen Binary Search; Midpoint; Inclusive/Exclusive;](https://frontendmasters.com/courses/algorithms/binary-search-algorithm/)

- [My Code in JS Kata Machine Day 2, Hint - look at Day 1 code as well](https://github.com/DaudIbrahim/dsa-js/blob/main/kata-machine/src/day2/BinarySearchList.ts)

- [Binary search can only be implemented on sorted data.](https://shorturl.at/dwNQZ)

- Midpoint

  ****- [getMidIndex via `getMidPointWithLowInclusiveAndHighExclusive`](https://github.com/DaudIbrahim/dsa-js/blob/main/kata-machine/src/day2/BinarySearchList.ts#L33)

  ```js
  /**
  - To find the mid in a list this is the approach I have decided to go with - thePrimeagen's mid method
  - ThePrimeagen's mid method, easy to remember about offsets
  - High is exclusive | Offset by one - this midpoint implementation uses low as an offset
  - Additionally: AWS for pagination includes offet, MySQL in its query for pagination makes use of OFFSET
  */
  const getMidPointWithLowInclusiveAndHighExclusive = (lowInclusive: number, highExclusive: number): number => {
      const response = lowInclusive + ((highExclusive - lowInclusive) / 2)
      return Math.floor(response)
  }
  ```

- *Establish the mental model of having your index off by 1's | inclusive/exclusive [low, high) range[0, 5)*

- Index: *Offset by One* | *useMemorize* | The phrase "offset by one" typically refers to a situation where something is shifted or adjusted by a single unit or increment.

A note on Set Theory

- Closed Interval

  - [a, b] - a & b both are included in the interval

- Half-open Interval

  - [a, b) - a is included & b is not, b is excluded from the interval

    Half Interval Python Example

    ```py
    for i in range(0, 5):
      print(i) # 0, 1, 2, 3, 4
    ```

- Big O - O (Log N)

## Sort

### Quick Sort (< Pivot <=)

- Divide and Conquer

  - Partition the array into two parts, partition one to the left and other to the right

    - Pivot Partition Key. Select an index/value to do the partition. There are more than one ways to pivotPartition. I have used the approach of using the last index as the pivot point aka... memory hook: Partition Key. (Similar to the idea of partition key in system design database sharding)

      - I am using the approach from [VisuAlgo NUS](https://visualgo.net/en/sorting)

        - Memorize the approach from [VisuAlgo NUS](https://visualgo.net/en/sorting) to solve for pivotPartition

          - **< Pivot <=**

          - **The pivotPartition Transforms [7, 1, 10, 3, 5] into [< Pivot <=]**

## Binary Search Tree

BST's key characteristic is that for each node, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value.

- Left Node
- Right Node

[Example of Binary Tree in Code](../kata-machine/src/__tests__/tree.ts)

## Binary Heap

Super cool data strcture that changes you perspective. [That has to do with the ability to change your perspective.](https://youtu.be/ZQElzjCsl9o?t=324)

[Heap is the data structure best suited to implement Priority Queues.](https://anmolsehgal.medium.com/heap-vs-priority-queues-vs-queues-b03398312c87#:~:text=Heap%20is%20the%20data%20structure%20best%20suited%20to%20implement%20Priority%20Queues.)

[What is a Binary Heap (Concept)](https://youtu.be/AE5I0xACpZs?si=y-Oh_rpBCfk1MT9i)

### Details

The problem that is being solved - create a queue that has an order of priority for its elements

Binary Heaps are implemented as a complete tree ("filling each level from left to right")
We are not Traversing instead accessing the parent and child by making use of indexes and mathematical formulas (pattern -> formula)

### Traversal

It is not exactly a tree traversal, rather we use mathematical formula to access left and right child; & parent from child

- Left Child

  - 2i + 1

- Right Child

  - 2i + 2

- Parent

  - (i - 1) / 2

### Operation

- Insert: Heapify Up

- Delete: Heapify Down

  - Memorize to compare children nodes before so that you heapify down to the correct node, in case of min heap, heapify down to the smaller node; this ensures that the the node with the samllest value remains at the top

## [Graph Theory Quintessential](https://youtube.com/playlist?list=PLpXOY-RxVRTPPVLBP6-sz6CMWxhtrI-v_)

- Intro
- Depth First
- Breadth First
- The Traveling Salesman Problem

## Traversal & Search

Graphs are a more general data structure that can include trees as a special case.

Traversal and Search are two fundamental operations used in working with graphs and trees.

The key conceptual difference between traversal and search lies in their primary objectives and how they navigate the tree structure. Traversal aims to visit all nodes in a systematic way, while search aims to find a specific node or satisfy a particular condition efficiently. The choice between traversal and search depends on the problem you're trying to solve with the tree or graph data structure.

- **Search**:

  - **Purpose**: Search involves finding a specific node or element within a tree or graph, often with a particular goal or criteria in mind. The objective is to locate a target node efficiently. [The algorithms in this class are Depth First Search (DFS), Breadth First Search (BFS), and Dijkstra’s algorithm. If you have additional time, I recommend you learn the A* algorithm as well.](https://levelup.gitconnected.com/must-know-algorithms-for-coding-interviews-937d807064e0#:~:text=The%20algorithms%20in%20this%20class%20are%20Depth%20First%20Search%20(DFS)%2C%20Breadth%20First%20Search%20(BFS)%2C%20and%20Dijkstra%E2%80%99s%20algorithm.%20If%20you%20have%20additional%20time%2C%20I%20recommend%20you%20learn%20the%20A*%20algorithm%20as%20well.)

  - **Types**: Here are two common types of tree search:

    - **Breadth-First Search (BFS)**: BFS starts at the root node and explores all neighbor nodes at the current depth level before moving on to nodes at the next depth level. It's typically used for finding the shortest path or for exploring all possible paths in an unweighted graph.

      - **Exploration Strategy**: BFS explores a graph by visiting all neighbors of a node before moving on to their children. It explores nodes at the current depth level before proceeding to nodes at the next depth level.

      - **Data Structure**: BFS uses a queue data structure to keep track of nodes to visit. Nodes are enqueued (added to the back of the queue) when they are discovered and dequeued (removed from the front of the queue) when they are visited.

      - **Use Cases**:
        - Finding the shortest path in an unweighted graph: Since BFS explores nodes level by level, the first time you encounter the target node, you can be sure that it is the shortest path.
        - Exploring all possible paths from a source node to a target node.
        - Discovering connected components in an unweighted graph.

      - **Completeness**: BFS is complete, meaning it will find a target node if it exists, provided the graph is connected.

    - **Depth-First Search (DFS)**: DFS explores as far as possible along a branch before backtracking. It can be implemented using recursion or a stack data structure. DFS is often used for tasks like checking if a path exists between two nodes or for topological sorting. **Depth-First preserves the shape of the traversal**

      - **Exploration Strategy**: DFS explores a graph by following a single branch as deeply as possible before backtracking. It explores one branch entirely before moving on to the next sibling branch.

      - **Data Structure**: DFS can be implemented using either recursion or a stack data structure. In a recursive DFS, each recursive call explores a node's children.

      - **Use Cases**:
        - Determining whether a path exists between two nodes.
        - Topological sorting: Ordering nodes in a directed acyclic graph (DAG) such that for every directed edge (u, v), node u comes before node v in the ordering.
        - Finding cycles in a graph.
        - Generating all possible solutions in problems like maze-solving or the N-Queens problem.

      - **Completeness**: DFS may not be complete in all cases, especially if there are cycles in the graph. It can get stuck in an infinite loop if not carefully implemented.

  In summary, BFS explores nodes level by level, making it suitable for tasks like finding the shortest path, while DFS explores one branch deeply before backtracking, making it suitable for tasks like finding paths and detecting cycles. The choice between BFS and DFS depends on the specific problem and the characteristics of the graph being traversed or searched.

- [**Tree Traversal**](https://youtu.be/b_NjndniOqY)

  Traversal and search are two fundamental operations used in working with tree data structures, such as binary trees. In case of traversal you traverse the entire tree and for search lookup a specific value.

  **Depth First Search**: DFS is the most common way to traverse trees. There are three ways to traverse a tree using DFS: in-order traversal, pre-order traversal, and post-order traversal. Each of these implementations are DFS and explore down a path fully. The only difference is the order in which they use the current node's data.

  **Purpose**: Tree traversal is the process of visiting and examining all nodes in a tree or graph in a systematic way without any specific goal of finding a particular node. The primary objective is to visit every node once.

  **Types**: [There are three common types of tree traversal using DFS](https://rb.gy/2j225):

  There are three common types of tree traversals: preorder, inorder, and postorder. Each traversal has a different order in which it visits nodes. Let's explore each of them in more detail:

  1. **Preorder Traversal**:
      - **Order of Visitation**: In preorder traversal, you visit the current node before its children. The order is as follows:
        1. Visit the current node.
        2. Traverse the left subtree (recursively).
        3. Traverse the right subtree (recursively).
      - **Common Uses**:
        - Preorder traversal is often used for copying a tree or generating a prefix expression from an expression tree.
        - It's also useful for certain types of binary tree constructions.

  2. **Inorder Traversal**:
      - **Order of Visitation**: In inorder traversal, you visit the left child, then the current node, and finally the right child. The order is as follows:
        1. Traverse the left subtree (recursively).
        2. Visit the current node.
        3. Traverse the right subtree (recursively).
      - **Common Uses**:
        - Inorder traversal is commonly used for binary search trees (BSTs) to retrieve elements in sorted order.
        - It helps in evaluating expressions represented as binary expression trees (infix expressions).

  3. **Postorder Traversal**:
      - **Order of Visitation**: In postorder traversal, you visit the children of a node before visiting the node itself. The order is as follows:
        1. Traverse the left subtree (recursively).
        2. Traverse the right subtree (recursively).
        3. Visit the current node.
      - **Common Uses**:
        - Postorder traversal is often used for tasks like deleting a tree because it ensures that you delete child nodes before their parent nodes.
        - It can also be used for certain tree transformations and calculations.

      Here's a simple example to illustrate these traversals on a binary tree:

      ```plaintext
              A
            /   \
            B     C
          / \   / \
          D   E F   G

      Preorder Traversal: A, B, D, E, C, F, G
      Inorder Traversal: D, B, E, A, F, C, G
      Postorder Traversal: D, E, B, F, G, C, A
      ```

      The order in which nodes are visited in each traversal type is crucial for various operations involving trees, and choosing the right traversal depends on the specific problem or task you want to solve.

      [So in summary, always go from the root in counterclockwise direction around the tree.](https://www.youtube.com/watch?v=WLvU5EQVZqY&lc=UgxwHLh8RDXYgk1hHyp4AaABAg.9YEq1NFsZT09toOL6s_7fS)
      - For Pre-Order, print the nodes as you visit them for the first time.
      - For In-Order, print the nodes only when you visit them for the second time.
      - For Post-order, print the nodes when you visit them for the last time.

  **Breadth-First Search**: BFS traverses the tree by level and can also be called [level-order traversal](https://skilled.dev/course/tree-traversal-in-order-pre-order-post-order). So it will go all the way through level 1, then level 2, and follow this path until it reaches the last level. BFS is used to find the shortest path to a node.

  ```plaintext
          A
        /   \
        B     C
      / \   / \
      D   E F   G

  Level Order Traversal: A, B, C, D, E, F, G
  ```

- **Tree Traversal, Graph Traversals & Cycles**

  In *a tree traversal*, such as DFS or BFS, there is no need to maintain a separate `seen array` or `visited list`. This is because trees are inherently acyclic structures, meaning there are no cycles or loops within the tree. When traversing a tree, whether using depth-first search (DFS) or breadth-first search (BFS), you naturally move from one node to its children or neighboring nodes. Since there are no cycles in a tree, you will not encounter the same node twice during the traversal. The absence of cycles ensures that you won't get stuck in an infinite loop while traversing a tree. Each node in a tree has a unique path to reach it from the root, so there is no need for additional checks to prevent revisiting nodes.

  However, in *a general graph traversal* (not limited to trees) where cycles are possible, maintaining a separate data structure like a `seen array` or `visited list` is necessary to keep track of visited nodes and prevent revisiting them. This helps avoid getting stuck in cycles or infinite loops.

  Examples of make use of a `seen array` or `visited list` in Graph

  - [BFSGraphMatrix](../kata-machine/src/day2/BFSGraphMatrix.ts)
  - [DFSGraphList](../kata-machine/src/day2/DFSGraphList.ts)
  - [DijkstraList.ts](../kata-machine/src/day2/DijkstraList.ts.ts)

## Dijkstra's Algorithm

Okay, so let's talk about Dijkstra's shortest path. It's actually a family of what is referred to as a greedy algorithm.

## Composing Data Structures

### LRU

- LRU

## [Greedy, Divide and Conquer, Dynamic & Backtracking](https://www.youtube.com/playlist?list=PLxvbXPxg6ydxQen2-cPMyzKco1Q89JvPi)

Silly memory hook: Greatly Designed Data Base - (GDDB) in order to Memorize the following four techniques:

### Greedy

The Greedy Approach

#### Algorithms that use The Greedy Approach

- Linear Search
  - Now, we need to just do the Undo function, which involves merging, hence the name, Merge Sort. All right, there are a bunch of different algorithm strategies. I didn't technically really name any of the algorithm strategies as we go, there's greedy. So linear search is a greedy search. We go until we find the first one, we're done.[(Src: theprimeagen-quicksort-algorithm-frontendmasters)](https://frontendmasters.com/courses/algorithms/quicksort-algorithm/)

- Dijkstra's shortest path, It's actually a family of what is referred to as a greedy algorithm.
  - [How Dijkstra's Algorithm Works: YT](https://youtu.be/EFg3u_E6eHU)
  - [dijkstra_list in kata-machine](../kata-machine/src/day2/DijkstraList.ts)

### Divide and Conquer

- Partition by Splitting (Splitting in half for example)
- Pivot Go: Left || Right

#### Algorithms that use The Divide and Conquer Approach

Binary Search, Quick Sort, & Binary Search Tree, share an identical Paradigm. **The Paradigm of Divide and Conquer**

- Binary Searh
- Quick Sort
- Binary Tree

### Dynamic Programming

*Essence* - `Dynamic programming is about finding solution to problems in recursive manner and then removing the overhead of recursion by various ways for example - Memoization, Bottom-up approach, Finding patterns, Deriving explicit formulas or equations.`

#### [What is Dynamic Programming and how is it done](https://youtu.be/BCO8JKA2_N8)

Steps

1. **Find The Recursive Solution**: Dynamic Programming often starts with defining a problem in a recursive way, where the solution depends on the solutions to smaller instances of the same problem.

2. **Try to find if there is a lot of repetitive states in it**: Dynamic Programming focuses on recognizing when the same subproblems are being solved multiple times. This is a key insight in many DP problems.

3. **Store them in Matrix**: Instead of recomputing the solutions for those repetitive subproblems, Dynamic Programming stores the results in a data structure like a matrix or table. This is known as memoization.

4. **Don't need to recompute the same thing again and again**: By storing the results of subproblems, Dynamic Programming avoids redundant calculations.

5. **Just store it, and that's what Dynamic programming is!! Simply put!!!**: This step nicely summarizes the essence of Dynamic Programming. It's about storing and reusing solutions to subproblems to optimize the overall problem-solving process.

Probelm Set

- Starting with easy DP problem - Longest common Sub Sequence / Sub String.
- Complex Problem - Bellman Ford

### Backtracking

Backtracking is a problem-solving technique that's like playing a game of "guess and check" to find a solution.

Imagine you have a big maze on a piece of paper, and you want to find your way from the start to the finish. You start by taking a step and see if it leads you closer to the finish. If it does, you keep going in that direction. But if you reach a dead-end or get stuck, you backtrack, which means you go back to where you made a different choice and try a different path. You keep doing this until you find a way to the finish.

Backtracking is like exploring different paths, trying things out, and if they don't work, going back to where you made a different choice and trying a new path. It's a technique used for solving problems where you have to explore many possibilities to find the best solution. Some common problems that can be solved with backtracking include:

1. **Mazes**: Finding a way out of a maze, like the one on your paper.

2. **N-Queens Puzzle**: Placing N chess queens on an N×N chessboard so that no two queens threaten each other.

3. **Sudoku**: Filling in a Sudoku puzzle with the right numbers while following certain rules.

4. **Permutations and Combinations**: Finding all possible orders or selections of a set of items.

5. **Traveling Salesman Problem**: Finding the shortest route that visits a set of cities and returns to the starting city.

6. **Cryptarithmetic Puzzles**: Solving puzzles where letters represent numbers in mathematical equations.

Backtracking is a way to be systematic and explore different options until you find the best one. It's like a game of trial and error where you learn from your mistakes and keep going until you find the answer. Backtracking is a general technique used for systematically exploring possibilities and is often employed in `solving combinatorial problems`.

## [Patterns for Solving Data Structures and Algorithms Problems](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)

- [NeetCode RoadMap](https://neetcode.io/roadmap?utm_source=linkedin)

### Pattern 0: Frequency Counter Pattern

### Pattern 1: Multiple Pointers by Colt Stelee

[Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition](https://cs.slides.com/colt_steele/problem-solving-patterns#/33)

Hint: useful in solving problems related to finding **Pairs**

### Pattern 2: Sliding Window

Hepls in solving *Hint* **Contiguous**

In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size.

## Misc

- <https://medium.com/dare-to-be-better/5-steps-of-problem-solving-approach-d891d6c1ae10>

### Keywords

- Refer

- Memorize

- Lessons Learnt

### Refer (Previously learned ideas & concepts)

- Start by fiding a solution for the smallest problem

  - Start by solving for the base case

  - Walk through the algorithm like ["Animator vs. Animation"](https://youtu.be/B1J6Ou4q8vE)

- middle-element

  - [getMidIndex via `getMidPointWithLowInclusiveAndHighExclusive`](https://github.com/DaudIbrahim/dsa-js/blob/main/kata-machine/src/day2/BinarySearchList.ts#L33)

  ```ts
  /**
  - To find the mid in a list this is the approach I have decided to go with - thePrimeagen's mid method
  - ThePrimeagen's mid method, easy to remember about offsets
  - High is exclusive | Offset by one - this midpoint implementation uses low as an offset
  - Additionally: AWS for pagination includes offet, MySQL in its query for pagination makes use of OFFSET
  */
  const getMidPointWithLowInclusiveAndHighExclusive = (lowInclusive: number, highExclusive: number): number => {
      const response = lowInclusive + ((highExclusive - lowInclusive) / 2)
      return Math.floor(response)
  }
  ```

- `OFFSET 🌟`

  - Binary Search approach *offset* exclusive high index. Crossing point of both pointers low and high becomses base case.
  - In a SinglyLinkedList we make use of offsetNode. (offsetNode - get the prev node to the current in order to update pointers)
  - MySQL Query for pagination makes use of *OFFSET*
  - AWS for pagination makes use of *offset*
  - Time zone UTC *offsets*

- nested loop

  - nested loops are to be avoided wherever and as much as possible use two pointers, sliding window, & fast and slow pointers

- database sharding

  1. Split Data - find a way to split your data into independant buckets

  2. Select a sharding key - based on your sharding key the load distribution will take place on the server

  3. Mapping Method - Mapping key to real servers
