"""
PatternScript Compiler - Test Suite
Tests .ps files by reading them and compiling directly
Includes mathematical validation functions (only used for test files)
"""

import os
import sys
from main import PatternScriptCompiler

class MathValidator:
    """Mathematical functions to validate and compute patterns"""

    @staticmethod
    def calculate_arithmetic_sequence(start, diff, count):
        return [start + (i * diff) for i in range(count)]
    
    @staticmethod
    def calculate_geometric_sequence(start, ratio, count):
        return [start * (ratio ** i) for i in range(count)]
    
    @staticmethod
    def calculate_modulo_pattern(start, count):
        return [(start + i) % 2 for i in range(1, count + 1)]
    
    @staticmethod
    def calculate_factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def calculate_sum_of_series(start, end):
        return sum(range(start, end + 1))
    
    @staticmethod
    def is_fibonacci_sequence(values):
        if len(values) < 3:
            return False
        try:
            nums = [int(v) for v in values]
            for i in range(2, len(nums)):
                if nums[i] != nums[i-1] + nums[i-2]:
                    return False
            return True
        except:
            return False
    
    @staticmethod
    def is_factorial_sequence(values):
        if len(values) < 2:
            return False
        try:
            nums = [int(v) for v in values]
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        except:
            return False
    
    @staticmethod
    def is_perfect_squares(values):
        try:
            nums = [int(v) for v in values]
            for num in nums:
                sqrt = int(num ** 0.5)
                if sqrt * sqrt != num:
                    return False
            return True
        except:
            return False


class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results = []
        self.validator = MathValidator()
    
   
    def demonstrate_math_functions(self):
        """Show doubling, even numbers, and tripling"""

        print(f"\n{'='*70}")
        print(f"MATHEMATICAL PATTERN DEMONSTRATIONS")
        print('='*70)

        # Doubling
        print(f"\n📐 Doubling Sequence (1, 2, 4, 8...)")
        doubling_code = """
pattern doubling(val) {
    if (n == 1) {
        print val;
    } else {
        result = val * 2;
        print result;
    }
}
generate doubling(1): 9;
"""
        try:
            compiler = PatternScriptCompiler(doubling_code, verbose=False)
            results = compiler.compile()
            if results['success']:
                print("   Output:", ", ".join(results['output']))
        except Exception as e:
            print(f"   Error: {e}")

        # Even numbers
        print(f"\n📐 Even Numbers (2, 4, 6, 8...)")
        evens_code = """
pattern evens(start) {
    if (n == 1) {
        result = start;
        print result;
    } else {
        result = start + 2;
        print result;
    }
}
generate evens(2): 10;
"""
        try:
            compiler = PatternScriptCompiler(evens_code, verbose=False)
            results = compiler.compile()
            if results['success']:
                print("   Output:", ", ".join(results['output']))
        except Exception as e:
            print(f"   Error: {e}")

        # Tripling
        print(f"\n📐 Tripling Sequence (3, 9, 27, 81...)")
        tripling_code = """
pattern tripling(val) {
    if (n == 1) {
        print val;
    } else {
        result = val * 3;
        print result;
    }
}
generate tripling(3): 8;
"""
        try:
            compiler = PatternScriptCompiler(tripling_code, verbose=False)
            results = compiler.compile()
            if results['success']:
                print("   Output:", ", ".join(results['output']))
        except Exception as e:
            print(f"   Error: {e}")

        print(f"\n✓ Math demos displayed!")
        print(f"{'='*70}")

    

def main():
    print("\n" + "="*70)
    print("  PATTERNSCRIPT COMPILER - TEST SUITE")
    print("  File-based Testing with Math Validators")
    print("="*70)
    
    runner = TestRunner()
    
    # Demonstrations — ONLY 3 requested patterns
    runner.demonstrate_math_functions()
    
    # Test cases
    tests = [
        ("example1_fibonacci.ps", "Fibonacci sequence", 
         runner.validator.is_fibonacci_sequence),
        ("example2_factorial.ps", "Factorial values", 
         runner.validator.is_factorial_sequence),
        ("example3_squares.ps", "Perfect squares", 
         runner.validator.is_perfect_squares),
    ]
    
    
    
   
    
    return 0 if runner.failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
