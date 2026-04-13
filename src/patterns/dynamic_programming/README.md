# Dynamic Programming — Blueprint

DP is a method for solving optimization and counting problems by defining a **state space** over subproblems with overlapping structure, then computing answers via memoization or tabulation.

## Beginner DP

### Beginner DP Template

1. Define the subproblem
2. Identify base cases
3. Write the recurrence: dp[n] = f(dp[n-1], dp[n-2], ...)
4. Choose top-down (memo dict) or bottom-up (dp array)

- _top-down_ → big to small, recursion + hash table
- _bottom-up_ → small to big, loop + array

### A Beginner mental model

The real skill in DP is:

1. What is the "state"? (what do I need to remember?)
2. What are valid transitions between states?
3. What order do I evaluate states so dependencies are ready?
4. Is the naive complexity acceptable, or do I need an optimization?

---

## The Core Mental Model

> **DP is graph traversal over a state space.**

Every DP problem is secretly a directed graph. Once you see this, everything else follows naturally:

| DP Concept   | Graph Meaning                      |
| ------------ | ---------------------------------- |
| State        | Node                               |
| Transition   | Directed edge                      |
| Base case    | Source / terminal node             |
| Answer       | Best path / count / reachability   |
| Memoization  | Caching already-visited nodes      |
| Bottom-up DP | Topological traversal of the graph |

**Top-down DP** → DFS on the state graph, cache visited nodes  
**Bottom-up DP** → Topological traversal of the same graph, explicit order

This unifies every DP type:

- 1D DP → line graph
- Grid DP → 2D lattice graph
- Knapsack → subset hypercube
- Interval DP → DAG over intervals `[i, j]`, edges are split points
- Tree DP → rooted tree, post-order traversal = bottom-up DP
- Bitmask DP → hypercube graph, edges add/remove elements

---

## The Blueprint

```txt
Step 0  Recognize DP applies
        ├─ optimal substructure: big answer builds from smaller answers
        └─ overlapping subproblems: same states are revisited → caching pays off

Step 1  Define the state  ★ hardest and most important step
        ├─ dp[state] means: "____"  ← write this in plain English first
        ├─ ask: "if I were paused here, what do I need to continue correctly?"
        ├─ a valid state must be:
        │    · sufficient  — fully determines future decisions
        │    · minimal     — no redundant information
        │    · Markovian   — future depends only on this state, not the past
        ├─ too few variables → wrong transitions
        ├─ too many variables → exponential blowup
        └─ common shapes: dp[i], dp[i][j], dp[mask], dp[i][j] for intervals

Step 2  Identify base cases
        ├─ terminal nodes in the state graph — no further transitions
        ├─ smallest inputs where the answer is directly known
        └─ wrong here = wrong everywhere above

Step 3  Write the transition  (edges in the graph)
        ├─ what choices exist at this state?
        ├─ where does each choice lead?
        ├─ dp[state] = max / min / sum / count over all choices
        └─ if this feels forced or messy → your state is wrong, go back to Step 1

Step 4  Determine evaluation order  (topological order of the graph)
        ├─ look at your transition — Which states does dp[state] depend on? Those must be computed first
        ├─ those must be computed first
        ├─ order is a consequence of transitions, not a separate decision
        ├─ top-down: recursion + memo dict (order is implicit, DFS handles it)
        └─ bottom-up: loop + dp array (you enforce the order explicitly)

Step 5  Complexity check  =  (# of states)  ×  (cost per transition)
        ├─ acceptable → done
        └─ too slow → look at the optimization layer below
```

---

## DP Structures As Graphs

| DP Type  | State Graph Shape                    | Traversal                   |
| -------- | ------------------------------------ | --------------------------- |
| 1D       | Line graph                           | Left to right               |
| Grid     | 2D lattice                           | Row by row                  |
| Knapsack | Subset hypercube                     | Increasing weight           |
| Interval | DAG on `[i,j]`, edges = split points | Increasing length           |
| Tree     | Rooted tree                          | Post-order (children first) |
| Bitmask  | Hypercube, edges = set transitions   | Increasing popcount         |

---

## Major DP Families

**Linear** — Fibonacci, house robber, simple recurrence chains  
**Knapsack** — 0/1, unbounded, bounded, multi-dimensional  
**String** — LCS, edit distance, palindrome DP, regex matching  
**Interval** — matrix chain multiplication, burst balloons  
**Tree** — diameter, max path sum, rerooting DP  
**Bitmask** — TSP, assignment problems  
**Graph/DAG** — shortest path with constraints, `k`-stop problems  
**Probability/EV** — expected value DP, game theory  
**Hybrid** — DP + binary search (LIS), DP + BFS/Dijkstra, DP + segment tree

---

## Optimization Layer

When naive DP is too slow, work through this in order:

**1. Can I reduce the state space?**
Remove unnecessary dimensions. Each dimension you drop is a multiplicative speedup.

**2. Can I simplify transitions?**

- Prefix sums → O(1) range-query transitions instead of a loop
- Rolling array → reduce memory when old states aren't needed

**3. Can I exploit structure in the transitions?**

| Technique               | When to reach for it                                |
| ----------------------- | --------------------------------------------------- |
| Monotonic deque         | Sliding window max/min in transitions; O(n²) → O(n) |
| Divide & Conquer DP     | Optimal split point is monotone across states       |
| Convex Hull Trick (CHT) | Transitions are linear functions of previous states |
| Binary search + DP      | LIS-style; patience sorting structure               |
| Matrix exponentiation   | Linear recurrence; compute dp[n] in O(m³ log n)     |

---

## Suggested Learning Path

| Stage        | Topics                                       |
| ------------ | -------------------------------------------- |
| Foundations  | 1D DP, Fibonacci variants, coin change       |
| Core         | Knapsack, LCS, LIS, grid DP                  |
| Intermediate | Interval DP, tree DP, bitmask DP             |
| Advanced     | CHT, D&C optimization, matrix exponentiation |

---

## Compact Solver Checklist

When sitting down with a new problem:

1. What are my **states** (nodes in the graph)?
2. What are my **transitions** (edges)?
3. What are the **base cases** (source / terminal nodes)?
4. What is the **evaluation order** (topological order)?
5. What is the **complexity** — states × cost per transition?
6. If too slow — which **optimization** matches the structure?

> If you can model a problem as shortest path, count, or reachability on a DAG of states — you already have a DP solution.
