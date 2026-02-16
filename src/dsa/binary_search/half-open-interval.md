# Why We Start Counting at Zero and Use [inclusive, exclusive) Bounds

[Reference: EWD831 "Why numbering should start at zero"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD831.html)
by Edsger W. Dijkstra (August 11, 1982)

## Half open interval

The name **half-open interval** — it comes from mathematics. Intervals have notation:

```txt
[a, b] → closed interval  — both ends included

(a, b) → open interval   — both ends excluded

[a, b) → half-open interval — left included, right excluded
```

## Quick example with half open interval

```py
# Array with 4 elements
arr = [10, 20, 30, 40]

# Half-open [0, 4) means indices 0,1,2,3
for i in range(0, 4):  # runs 4 times
    print(arr[i])

# Length = 4 - 0 = 4  ✓ (Benefit 1)
# No mental gymnastics needed!
```

## Note: length and index are distinct

```py
# length -> working with counts, counting world
# index -> working with indices, index world
```

## Why use ≤ for lower bound and < for upper bound (like `0 ≤ i < N`)

### Benefit 1: Length is easy to calculate

- Upper bound minus lower bound = length of sequence
- Example: `2 ≤ i < 13` → 13 - 2 = 11 elements
- No need to add or subtract 1!

### Benefit 2: Adjacent sequences connect perfectly

- When two sequences are next to each other, the upper bound of one equals the lower bound of the next
- Example: `0 ≤ i < 5` then `5 ≤ i < 10`
- No gaps, no overlaps, no confusion

### Benefit 3: Works naturally with zero (smallest natural number)

- Inclusive lower bound (≤) lets you start at 0 without problems
- Example: `0 ≤ i < 5` is clean
- But exclusive lower bound would force you to write `-1 < i < 5` (ugly - negative numbers aren't natural!)

### Benefit 4: Empty sequences work elegantly

- When a sequence has no elements, the notation still makes sense
- Example: `0 ≤ i < 0` clearly means "nothing"
- With inclusive upper bound you'd need unnatural numbers

## Why start counting at zero

### Benefit 5: Simpler range notation

- For N elements starting at 0: `0 ≤ i < N` (clean!)
- For N elements starting at 1: `1 ≤ i < N+1` (that +1 is annoying)

### Benefit 6: Index = number of preceding elements

- Element at position 0 has 0 elements before it
- Element at position 5 has 5 elements before it
- This is a natural, meaningful relationship!

### Benefit 7: Proven in practice

- Mesa programming language allowed all notations
- Programmers made constant mistakes with other conventions
- Only the 0-based, `≤...<` convention worked reliably
