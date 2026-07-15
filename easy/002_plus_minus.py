"""
Problem: Plus Minus
Source: HackerRank
Difficulty: Easy
Date: 2026-01-10

Description:
Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with 6
places after the decimal.

Examples:
arr = [-4, 3, -9, 0, 4, 1]
n = 6

Positive numbers: 3 (3, 4, 1) → 3/6 = 0.500000
Negative numbers: 2 (-4, -9) → 2/6 = 0.333333
Zeros: 1 (0) → 1/6 = 0.166667

Output:
0.500000
0.333333
0.166667

Constraints:
- 0 < n <= 100
- -100 <= arr[i] <= 100
"""

def plusMinus(arr):
    """
    Calculate and print ratios of positive, negative, and zero values.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    pass


# Test cases
if __name__ == '__main__':
    import io
    from contextlib import redirect_stdout

    def capture(arr):
        buf = io.StringIO()
        with redirect_stdout(buf):
            plusMinus(arr)
        return buf.getvalue()

    # Test case 1
    arr = [-4, 3, -9, 0, 4, 1]
    output = capture(arr)
    print(f"Test 1: arr = {arr}\n{output}", end='')
    assert output == "0.500000\n0.333333\n0.166667\n", f"Got: {output!r}"

    # Test case 2
    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    output = capture(arr)
    print(f"Test 2: arr = {arr}\n{output}", end='')
    assert output == "0.375000\n0.375000\n0.250000\n", f"Got: {output!r}"

    # Test case 3
    arr = [1, 1, 0, -1, -1]
    output = capture(arr)
    print(f"Test 3: arr = {arr}\n{output}", end='')
    assert output == "0.400000\n0.400000\n0.200000\n", f"Got: {output!r}"

    print("All tests passed!")
