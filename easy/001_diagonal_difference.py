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
    length = len(arr)-1
    midpoint = (length//2)

    L_sum = 0
    R_sum = 0
    position = 0

    for row in (arr):
        L_sum += row[position]
        R_sum += row[length-position]
        position +=1
    return abs(L_sum-R_sum)



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

    # Test case 4 - 5x5 matrix
    arr4 = [
        [1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 4, 0],
        [0, 0, 0, 0, 5]
    ]
    result4 = diagonalDifference(arr4)
    print(f"Test 4: {result4}")
    # Primary diagonal: 1+2+3+4+5 = 15
    # Secondary diagonal: 0+0+3+0+0 = 3
    # Difference: |15-3| = 12
    assert result4 == 12, f"Expected 12, got {result4}"

    print("All tests passed!")
