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

Now install the packages listed in your requirements file:

```bash
pip install -r requirements.txt
```

(Use `requirements.txt`, not `requirements.in` - the `.txt` file is the one with the actual versions)

## 6. Verify Installation

Check if ruff was installed:

```bash
ruff --version
```

That's it! Now you can start coding your DSA practice. Create a new `.py` file and start writing Python code.

**Quick tip for DSA:** Just create files like `arrays.py`, `linkedlist.py`, etc. and run them with `python filename.py`.
