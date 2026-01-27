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
    print("Test 1:")
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 6")
    print()

    # Test case 2
    print("Test 2:")
    height = [4,2,0,3,2,5]
    result = solution.trap(height)
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 9")
    print()

    # Test case 3
    print("Test 3:")
    height = [0,2,0]
    result = solution.trap(height)
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print()

    # Test case 4
    print("Test 4:")
    height = [3,0,2,0,4]
    result = solution.trap(height)
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 7")
    print()

    # Test case 5
    print("Test 5:")
    height = []
    result = solution.trap(height)
    print(f"Input: height = {height}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print()
