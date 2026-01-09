"""
Problem: Diagonal Difference
Source: HackerRank
Difficulty: Easy
Date: 2026-01-09

Description:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

The left-to-right diagonal (primary diagonal) runs from arr[0][0] to arr[n-1][n-1].
The right-to-left diagonal (secondary diagonal) runs from arr[0][n-1] to arr[n-1][0].

Examples:
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]

Primary diagonal: 1 + 5 + 9 = 15
Secondary diagonal: 3 + 5 + 9 = 17
Difference: |15 - 17| = 2

Constraints:
- Matrix is always n x n (square)
- -100 <= arr[i][j] <= 100
"""

def diagonalDifference(arr):
    """
    Calculate absolute difference between diagonal sums.

    Time Complexity: O(n) where n is the dimension of the matrix
    Space Complexity: O(1)
    """
    # Write your code here
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1
    arr1 = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
    result1 = diagonalDifference(arr1)
    print(f"Test 1: {result1}")
    assert result1 == 2, f"Expected 2, got {result1}"

    # Test case 2
    arr2 = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    result2 = diagonalDifference(arr2)
    print(f"Test 2: {result2}")
    assert result2 == 15, f"Expected 15, got {result2}"

    # Test case 3 - Single element
    arr3 = [[5]]
    result3 = diagonalDifference(arr3)
    print(f"Test 3: {result3}")
    assert result3 == 0, f"Expected 0, got {result3}"

    print("All tests passed!")
