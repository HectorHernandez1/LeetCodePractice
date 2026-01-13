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
    # Write your code here
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    arr1 = [1, 2, 3, 4, 5]
    miniMaxSum(arr1)
    # Expected output: 10 14
    print()

    # Test case 2
    print("Test 2:")
    arr2 = [7, 69, 2, 221, 8974]
    miniMaxSum(arr2)
    # Expected output: 299 9271
    print()

    # Test case 3
    print("Test 3:")
    arr3 = [5, 5, 5, 5, 5]
    miniMaxSum(arr3)
    # Expected output: 20 20
    print()

    # Test case 4
    print("Test 4:")
    arr4 = [1, 3, 5, 7, 9]
    miniMaxSum(arr4)
    # Expected output: 16 24
