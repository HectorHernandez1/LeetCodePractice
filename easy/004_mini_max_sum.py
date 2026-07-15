"""
Problem: Mini-Max Sum
Source: HackerRank
Difficulty: Easy
Date: 2026-01-13

Description:
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers. Then print the respective
minimum and maximum values as a single line of two space-separated long integers.

Examples:
arr = [1, 2, 3, 4, 5]

Calculate the following sums using four of the five integers:
- Sum everything except 1: 2 + 3 + 4 + 5 = 14
- Sum everything except 2: 1 + 3 + 4 + 5 = 13
- Sum everything except 3: 1 + 2 + 4 + 5 = 12
- Sum everything except 4: 1 + 2 + 3 + 5 = 11
- Sum everything except 5: 1 + 2 + 3 + 4 = 10

Minimum sum: 10
Maximum sum: 14
Output: 10 14

Constraints:
- Array length is always 5
- 1 <= arr[i] <= 10^9

Note: Beware of integer overflow! Use a 64-bit integer to store the sums.
"""

def miniMaxSum(arr):
    """
    Calculate and print the minimum and maximum sums of 4 out of 5 integers.

    Args:
        arr: an array of 5 integers

    Returns:
        None (prints the min and max sums)
    """
    pass

# Test cases
if __name__ == '__main__':
    import io
    from contextlib import redirect_stdout

    def capture(arr):
        buf = io.StringIO()
        with redirect_stdout(buf):
            miniMaxSum(arr)
        return buf.getvalue()

    # Test case 1
    arr = [1, 2, 3, 4, 5]
    output = capture(arr)
    print(f"Test 1: arr = {arr} -> {output.strip()} (expected 10 14)")
    assert output == "10 14\n", f"Got: {output!r}"

    # Test case 2
    arr = [7, 69, 2, 221, 8974]
    output = capture(arr)
    print(f"Test 2: arr = {arr} -> {output.strip()} (expected 299 9271)")
    assert output == "299 9271\n", f"Got: {output!r}"

    # Test case 3: all equal
    arr = [5, 5, 5, 5, 5]
    output = capture(arr)
    print(f"Test 3: arr = {arr} -> {output.strip()} (expected 20 20)")
    assert output == "20 20\n", f"Got: {output!r}"

    # Test case 4
    arr = [1, 3, 5, 7, 9]
    output = capture(arr)
    print(f"Test 4: arr = {arr} -> {output.strip()} (expected 16 24)")
    assert output == "16 24\n", f"Got: {output!r}"

    print("All tests passed!")
