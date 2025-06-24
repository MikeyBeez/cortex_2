#!/usr/bin/env python3
# /Users/bard/Code/cortex_2/run_tests.py
"""Test runner for Cortex_2"""
import sys
import subprocess
from pathlib import Path

def run_tests():
    """Run all tests with coverage"""
    print("🧪 Running Cortex_2 Tests...")
    print("-" * 50)
    
    # Ensure we're in the right directory
    root_dir = Path(__file__).parent
    
    # Run pytest with coverage using uv
    cmd = [
        "uv", "run", "pytest",
        "-v",  # Verbose
        "--cov=cortex",  # Coverage for cortex module
        "--cov-report=term-missing",  # Show missing lines
        "--cov-report=html",  # Generate HTML report
        "tests/"
    ]
    
    result = subprocess.run(cmd, cwd=root_dir)
    
    if result.returncode == 0:
        print("\n✅ All tests passed!")
        print("📊 Coverage report generated in htmlcov/index.html")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

def run_specific_test(test_path):
    """Run a specific test file or directory"""
    print(f"🧪 Running: {test_path}")
    print("-" * 50)
    
    cmd = [
        "uv", "run", "pytest",
        "-v",
        test_path
    ]
    
    subprocess.run(cmd)

def run_quick_tests():
    """Run only unit tests (fast)"""
    print("🏃 Running quick unit tests...")
    print("-" * 50)
    
    cmd = [
        "uv", "run", "pytest",
        "-v",
        "tests/unit/",
        "-m", "not slow"  # Skip slow tests if marked
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "quick":
            run_quick_tests()
        else:
            run_specific_test(sys.argv[1])
    else:
        run_tests()
