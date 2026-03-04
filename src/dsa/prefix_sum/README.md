# Prefix Sum Array and Range Sum Queries

## What a Prefix Sum Is

Given:

```py
arr = [a0, a1, a2, ..., a(n-1)]
```

A prefix sum array stores cumulative totals.

Two ways to define it.

## Model 1 — Normal Prefix (Length n)

```txt
prefix[i] = sum of elements from index 0 to i (inclusive)
```

Example:

```py
arr    = [2, 3, 5, 7]
prefix = [2, 5, 10, 17]
```

Range query:

```py
if l == 0:
    prefix[r]
else:
    prefix[r] - prefix[l-1]
```

Idea:

- `prefix[r]` contains everything from start to `r`
- subtract what comes before `l`
- slight edge case when `l == 0`

Works. Clear. Slight branching.

## Model 2 — Zero-Offset Prefix (Length n+1) ← The Winner

Define:

```text
P[0] = 0
P[i] = sum of first i elements
```

Meaning:

```text
P[i] = a0 + a1 + ... + a(i-1)
```

Example:

```python
arr = [2, 3, 5, 7]
P   = [0, 2, 5, 10, 17]
```

Interpretation:

- `P[0]` → sum of 0 elements
- `P[1]` → sum of first 1 element
- `P[4]` → sum of first 4 elements

This shifts thinking from:

Index world → Counting world.

That shift is everything.

### Counting World vs Index World

Index world:

- `arr[i]` means element at position `i`

Counting world:

- `P[i]` means how many elements are included

This aligns perfectly with half-open intervals:

```text
range(a, b) → includes a ... b-1
```

So:

```text
P[b] - P[a]
```

means:

Sum of elements from index `a` to `b-1`.

Always.

No edge case.
No condition.
No special handling.

### The Core Identity

In the zero-offset model:

```text
P[b] - P[a] = sum of indices a through b-1
```

**Why does this work?** Write out both prefix sums fully:

```text
P[b] = a0 + a1 + ... + a(a-1) + a(a) + a(a+1) + ... + a(b-1)
P[a] = a0 + a1 + ... + a(a-1)
```

Now subtract line by line:

```text
P[b] - P[a] = [a0 + a1 + ... + a(a-1)] + a(a) + ... + a(b-1)
            - [a0 + a1 + ... + a(a-1)]
            = a(a) + a(a+1) + ... + a(b-1)
```

The shared prefix — everything before index `a` — cancels exactly.
What survives is precisely the slice you wanted.

This isn't magic. It's just that `P[b]` contains `P[a]` inside it.
Subtraction peels off the part you don't need.

#### Core Identity Example

```python
arr    = [2, 5, 3, 7]
prefix = [0, 2, 7, 10, 17]

# Sum from index 1 to 3 inclusive → translate to [1, 4)
result = prefix[4] - prefix[1]  # 17 - 2 = 15

# Verify
print(result)          # 15
print(sum(arr[1:4]))   # 15 ✓
```

### Handling Inclusive Queries

If asked:

```text
sum from l to r inclusive
```

Translate to half-open:

```text
[l, r+1)
```

Then compute:

```text
P[r+1] - P[l]
```

Example — sum from index 2 to 4:

```text
P[5] - P[2]
```

Single element (index 5 to 5):

```text
P[6] - P[5]
```

Same rule.
Always.

### Why Zero-Offset Wins

It:

- Eliminates branching (`l == 0`)
- Aligns with half-open intervals
- Matches Python's `range`
- Scales cleanly to 2D prefix sums
- Scales to difference arrays
- Scales to hash-map prefix problems
- Feels algebraically natural

Most importantly:

It separates counting from indexing.

That separation reduces off-by-one errors dramatically.

### The Deep Insight

Prefix sums are not a trick.

They are:

Storing cumulative totals so subtraction cancels unwanted portions.

That's the whole structure.

Everything else — indices, offsets, `+1` — is bookkeeping.

## Conclusion

Arrived at zero-offset not by memorization,
but by unifying:

- Half-open intervals
- Counting vs index world
- Cancellation logic
- Clean algebraic identity

That's real understanding.

You don't need to re-prove it every time.

Just remember the identity:

```text
P[b] - P[a] = sum of a ... b-1
```

Everything else follows.
