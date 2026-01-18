#!/usr/bin/env python3
"""
Kata Machine Test Runner
========================
This is your test runner script - like 'npm test' in JavaScript!

Usage:
    python kata.py                  # Run all tests in kata/
    python kata.py binary_search    # Run tests for specific algorithm
    python kata.py merge_sort       # Run tests for merge_sort (when you create it)

How it works:
    - Uses sys.argv to read command-line arguments (like process.argv in Node.js)
    - Calls pytest programmatically to run tests
    - Automatically finds the right test files based on your input
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Main entry point for the kata test runner"""
    
    # Get the kata directory path
    kata_dir = Path(__file__).parent / "kata"
    
    # Check if kata directory exists
    if not kata_dir.exists():
        print("❌ Error: kata/ directory not found!")
        print("Make sure you're running this from the project root.")
        return 1
    
    # sys.argv is a list: [script_name, arg1, arg2, ...]
    # Example: python kata.py binary_search
    #   sys.argv = ['kata.py', 'binary_search']
    
    if len(sys.argv) > 1:
        # User specified an algorithm to test
        algorithm = sys.argv[1]
        test_path = kata_dir / algorithm
        
        if not test_path.exists():
            print(f"❌ Error: Algorithm '{algorithm}' not found in kata/")
            print(f"Available algorithms:")
            for item in sorted(kata_dir.iterdir()):
                if item.is_dir() and not item.name.startswith('.'):
                    print(f"  - {item.name}")
            return 1
        
        print(f"🧪 Running tests for: {algorithm}")
        print(f"📁 Test path: {test_path}")
        print("-" * 50)
    else:
        # No argument provided, test everything
        test_path = kata_dir
        print("🧪 Running ALL tests in kata/")
        print("-" * 50)
    
    # Run pytest
    # subprocess.run() is like running a command in terminal
    # [sys.executable, '-m', 'pytest'] ensures we use the right Python interpreter
    result = subprocess.run(
        [sys.executable, '-m', 'pytest', str(test_path), '-v'],
        cwd=Path(__file__).parent
    )
    
    # Return the exit code (0 = success, non-zero = failure)
    return result.returncode


if __name__ == "__main__":
    # This runs when you execute: python kata.py
    # (like if (require.main === module) in Node.js)
    sys.exit(main())
