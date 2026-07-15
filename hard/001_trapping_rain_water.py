#!/bin/python3
"""
Problem: Trapping Rain Water
Source: LeetCode #42
Difficulty: Hard
Date: TBD

Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Function Description:
Complete the trap function with the following parameters:
    height: List[int] - array of non-negative integers representing elevation

Returns:
    int: total amount of trapped water

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Examples:

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: 6 units of water can be trapped (see diagram in LeetCode)

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculate trapped water using two-pointer approach.

        Args:
            height: List of non-negative integers representing elevation

        Returns:
            int: Total amount of trapped water
        """
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(height)
    print(f"Test 1: {height} -> {result} (expected 6)")
    assert result == 6, f"Got: {result}"

    # Test case 2
    height = [4, 2, 0, 3, 2, 5]
    result = solution.trap(height)
    print(f"Test 2: {height} -> {result} (expected 9)")
    assert result == 9, f"Got: {result}"

    # Test case 3: single valley too shallow to trap water
    height = [0, 2, 0]
    result = solution.trap(height)
    print(f"Test 3: {height} -> {result} (expected 0)")
    assert result == 0, f"Got: {result}"

    # Test case 4
    height = [3, 0, 2, 0, 4]
    result = solution.trap(height)
    print(f"Test 4: {height} -> {result} (expected 7)")
    assert result == 7, f"Got: {result}"

    # Test case 5: empty input
    height = []
    result = solution.trap(height)
    print(f"Test 5: {height} -> {result} (expected 0)")
    assert result == 0, f"Got: {result}"

    print("All tests passed!")
