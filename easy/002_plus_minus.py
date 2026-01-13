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
    total = len(arr)

    # for negative
    negative = []
    postive = []
    zeroes = []
    for n in arr:
        if n > 0:
            postive.append(n)
        elif n < 0:
            negative.append(n)
        else:
            zeroes.append(n)

    print(f"{len(postive)/total:.6f}")
    print(f"{len(negative)/total:.6f}")
    print(f"{len(zeroes)/total:.6f}")


# Test cases
if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    arr1 = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr1)
    print()  # Expected output:
             # 0.500000
             # 0.333333
             # 0.166667

    # Test case 2
    print("Test 2:")
    arr2 = [1, 2, 3, -1, -2, -3, 0, 0]
    plusMinus(arr2)
    print()  # Expected output:
             # 0.375000
             # 0.375000
             # 0.250000

    # Test case 3
    print("Test 3:")
    arr3 = [1, 1, 0, -1, -1]
    plusMinus(arr3)
    print()  # Expected output:
             # 0.400000
             # 0.400000
             # 0.200000
