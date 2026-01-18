# 🥋 Kata Machine - DSA Testing Guide

Welcome to your **Kata Machine**! This is your personal DSA practice environment with automated testing, inspired by [_ThePrimeagen_'s Frontend Masters' kata machine](https://frontendmasters.com/courses/algorithms/linear-search-kata-setup/).

---

## 📚 Table of Contents

1. [Quick Start](#-quick-start)
2. [How It Works](#-how-it-works)
3. [Folder Structure](#-folder-structure)
4. [Running Tests](#-running-tests)
5. [Creating New Algorithms](#-creating-new-algorithms)
6. [Understanding Pytest](#-understanding-pytest)
7. [JS to Python Testing Comparison](#-js-to-python-testing-comparison)
8. [Tips & Tricks](#-tips--tricks)

---

## 🚀 Quick Start

```bash
# Run all tests
python kata.py

# Run tests for a specific algorithm
python kata.py binary_search
```

That's it! Focus on writing algorithm logic, let the tests guide you.

---

## 🎯 How It Works

### The Big Picture

```
You write algorithm → Tests run automatically → Get instant feedback
```

Just like Frontend Masters' kata machine, but for Python!

### What You Do

1. Navigate to an algorithm folder (e.g., `kata/binary_search/`)
2. Write your implementation in `binary_search.py`
3. Run `python kata.py binary_search`
4. Fix errors, repeat until all tests pass ✅

### What AI Does (Me!)

- Sets up all the testing infrastructure
- Writes comprehensive test cases
- Maintains the test runner script
- Handles all Python package stuff

---

## 📁 Folder Structure

```
kata/
├── binary_search/
│   ├── binary_search.py           # ← Your implementation goes here
│   └── test_binary_search.py      # ← Test cases (AI-generated)
├── merge_sort/                     # ← Future algorithm
│   ├── merge_sort.py
│   └── test_merge_sort.py
└── README.md                       # ← You are here!

kata.py                             # ← Test runner (like npm test)
```

### File Naming Convention

| JavaScript (Jest) | Python (Pytest)         | Purpose        |
| ----------------- | ----------------------- | -------------- |
| `index.js`        | `binary_search.py`      | Implementation |
| `index.test.js`   | `test_binary_search.py` | Tests          |

**Important:** Pytest requires test files to start with `test_` or end with `_test.py`

---

## 🧪 Running Tests

### Command Syntax

```bash
python kata.py [algorithm_name]
```

### Examples

```bash
# Test everything in kata/
python kata.py

# Test just binary search
python kata.py binary_search

# Test merge sort (when you create it)
python kata.py merge_sort
```

### Understanding Test Output

When you run tests, you'll see output like this:

```
🧪 Running tests for: binary_search
📁 Test path: /path/to/kata/binary_search
--------------------------------------------------
============================= test session starts ==============================
collected 11 items

test_binary_search.py::TestBinarySearch::test_finds_element_in_middle PASSED [ 9%]
test_binary_search.py::TestBinarySearch::test_finds_first_element PASSED [18%]
...
============================== 11 passed in 0.03s ===============================
```

**What this means:**

- ✅ `PASSED` = Test passed
- ❌ `FAILED` = Test failed (you'll see details about what went wrong)
- `11 passed` = All 11 test cases passed!

---

## 🆕 Creating New Algorithms

### Step-by-Step

1. **Create a new folder** in `kata/`:

   ```bash
   mkdir kata/merge_sort
   ```

2. **Create implementation file**:

   ```bash
   touch kata/merge_sort/merge_sort.py
   ```

3. **Create test file**:

   ```bash
   touch kata/merge_sort/test_merge_sort.py
   ```

4. **Ask AI for test cases**:

   > "Hey, write test cases for merge_sort in `kata/merge_sort/test_merge_sort.py`"

5. **Write your implementation** in `merge_sort.py`

6. **Run tests**:

   ```bash
   python kata.py merge_sort
   ```

---

## 🔬 Understanding Pytest

[Please Learn How To Write Tests in Python… • Pytest Tutorial](https://youtu.be/EgpLj86ZHFQ?si=bSZkSRzsyYlw47AT)

### What is Pytest?

**Pytest** is Python's most popular testing framework. Think of it as **Jest for Python**.

| Feature        | Jest (JS)                     | Pytest (Python)       |
| -------------- | ----------------------------- | --------------------- |
| Test files     | `*.test.js`                   | `test_*.py`           |
| Test functions | `test('name', () => {})`      | `def test_name():`    |
| Assertions     | `expect(x).toBe(y)`           | `assert x == y`       |
| Test suites    | `describe('Suite', () => {})` | `class TestSuite:`    |
| Run all tests  | `npm test`                    | `pytest`              |
| Run specific   | `npm test file`               | `pytest path/to/file` |

### Anatomy of a Test File

```python
# test_binary_search.py

import pytest                          # Import pytest (like importing Jest)
from binary_search import binary_search  # Import your function

class TestBinarySearch:                # Test suite (like describe() in Jest)
    """Test suite for binary search"""

    def test_finds_element(self):      # Test case (like test() in Jest)
        """Should find element in array"""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 3)
        assert result == 2             # Assertion (like expect().toBe())
```

### Key Concepts

#### 1. **Test Discovery**

Pytest automatically finds tests by looking for:

- Files named `test_*.py` or `*_test.py`
- Functions named `test_*()`
- Classes named `Test*`

#### 2. **Assertions**

In Jest:

```javascript
expect(result).toBe(2);
expect(result).toEqual([1, 2, 3]);
expect(result).toBeTruthy();
```

In Pytest:

```python
assert result == 2
assert result == [1, 2, 3]
assert result  # Truthy check
```

#### 3. **Test Organization**

```python
class TestBinarySearch:           # Group related tests
    def test_case_1(self):        # Individual test
        pass

    def test_case_2(self):
        pass
```

---

## 🔄 JS to Python Testing Comparison

### Jest Test (JavaScript)

```javascript
// binary_search.test.js
import { binarySearch } from "./binary_search";

describe("Binary Search", () => {
  test("finds element in middle", () => {
    const arr = [1, 2, 3, 4, 5];
    const result = binarySearch(arr, 3);
    expect(result).toBe(2);
  });

  test("returns -1 when not found", () => {
    const arr = [1, 2, 3];
    expect(binarySearch(arr, 5)).toBe(-1);
  });
});
```

### Pytest Test (Python)

```python
# test_binary_search.py
import pytest
from binary_search import binary_search

class TestBinarySearch:
    def test_finds_element_in_middle(self):
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 3)
        assert result == 2

    def test_returns_negative_when_not_found(self):
        arr = [1, 2, 3]
        assert binary_search(arr, 5) == -1
```

**Key Differences:**

- No `import` statement needed for `test` or `describe` in Jest
- Python uses `assert` instead of `expect()`
- Python uses `class` for test grouping instead of `describe()`
- Python uses `def` for test functions instead of arrow functions

---

## 💡 Tips & Tricks

### 1. **Verbose Output**

See more details about each test:

```bash
python kata.py binary_search -v
```

### 2. **Stop on First Failure**

Stop running tests after the first failure:

```bash
python kata.py binary_search -x
```

### 3. **Run Specific Test**

Run just one test function:

```bash
pytest kata/binary_search/test_binary_search.py::TestBinarySearch::test_finds_element_in_middle
```

### 4. **See Print Statements**

By default, pytest captures print output. To see it:

```bash
python kata.py binary_search -s
```

### 5. **Test-Driven Development (TDD)**

1. Read the test cases first
2. Understand what the function should do
3. Write your implementation
4. Run tests and iterate

### 6. **Debugging Failed Tests**

When a test fails, pytest shows you:

- Which test failed
- Expected vs actual values
- The line where it failed

Example:

```
FAILED test_binary_search.py::TestBinarySearch::test_finds_element_in_middle
AssertionError: assert None == 2
```

This means your function returned `None` but the test expected `2`.

---

## 🎓 How the Test Runner Works

### The Magic Behind `kata.py`

Remember how in JavaScript you run `npm test`? Here's what happens:

**JavaScript (npm):**

```json
// package.json
{
  "scripts": {
    "test": "jest"
  }
}
```

When you run `npm test`, npm reads `package.json` and executes `jest`.

**Python (kata.py):**

```python
# kata.py
import sys
import subprocess

# sys.argv captures command-line arguments
# Example: python kata.py binary_search
#   sys.argv = ['kata.py', 'binary_search']

algorithm = sys.argv[1] if len(sys.argv) > 1 else None

# subprocess.run() executes a shell command
subprocess.run(['python', '-m', 'pytest', f'kata/{algorithm}'])
```

### Command-Line Arguments in Python

In JavaScript (Node.js):

```javascript
// process.argv
// Running: node script.js arg1 arg2
console.log(process.argv);
// Output: ['node', 'script.js', 'arg1', 'arg2']
```

In Python:

```python
# sys.argv
# Running: python script.py arg1 arg2
import sys
print(sys.argv)
# Output: ['script.py', 'arg1', 'arg2']
```

**That's how `python kata.py binary_search` works!**

- `sys.argv[0]` = `'kata.py'`
- `sys.argv[1]` = `'binary_search'`

---

## 🎯 Your Workflow

1. **Pick an algorithm** to practice (e.g., binary search)
2. **Open the implementation file** (`kata/binary_search/binary_search.py`)
3. **Read the test file** to understand requirements
4. **Write your solution**
5. **Run tests**: `python kata.py binary_search`
6. **Fix errors** and repeat until all tests pass ✅
7. **Move to next algorithm** 🚀

---

## 📦 Dependencies

This kata machine uses:

- **pytest**: Testing framework (like Jest)
- **ruff**: Code linter (like ESLint)

Both are installed via `requirements.txt`.

---

## 🤝 Getting Help

If you're stuck:

1. Read the test cases - they show you what the function should do
2. Use print statements to debug: `print(f"Current value: {variable}")`
3. Run tests with `-s` flag to see print output
4. Ask AI for hints (but try to solve it yourself first!)

---

## 🎉 You're Ready

Now go write some algorithms! Remember:

- **Focus on logic** - that's what matters
- **Let tests guide you** - they're your feedback loop
- **Iterate quickly** - run tests often

Happy coding! 🚀

---

_Last updated: 2026-01-18_
