# Project Setup

## 1. Install Python

Make sure Python is installed on your computer. Open your terminal/command prompt and type:

```bash
python --version
```

or

```bash
python3 --version
```

If you don't have Python, download it from python.org (get Python 3.11 or newer).

## 2. Navigate to Your Project

Open terminal and go to your project folder:

```bash
cd path/to/your/project
```

## 3. Create a Virtual Environment (Important!)

This keeps your project dependencies separate:

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

**On Windows:**

```bash
venv\Scripts\activate
```

**On Mac/Linux:**

```bash
source venv/bin/activate
```

You'll see `(venv)` appear in your terminal prompt when it's activated.

## 5. Install Dependencies

Now install the packages:

```bash
pip install -r requirements.in
```

This will install `ruff` (linter) and `pytest` (testing framework).

## 6. Verify Installation

Check if ruff was installed:

```bash
ruff --version
```

That's it! Now you can start coding your DSA practice.

## 7. Testing Your DSA Code (Kata Machine)

This project includes a **kata machine** for testing your DSA implementations with pytest!

### Verify pytest installation

```bash
pytest --version
```

### Run tests

```bash
# Test all algorithms
python kata.py

# Test a specific algorithm (e.g., binary_search)
python kata.py binary_search
```

### How it works

1. Navigate to `kata/` folder
2. Each algorithm has its own folder (e.g., `kata/binary_search/`)
3. Write your implementation in the algorithm file (e.g., `binary_search.py`)
4. Run tests to get instant feedback
5. Fix errors and iterate until all tests pass ✅

For detailed testing guide, see: `kata/README.md`
