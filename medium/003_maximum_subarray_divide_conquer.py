#!/bin/python3
"""
Problem: Maximum Subarray (Divide and Conquer)
Source: LeetCode #53
Difficulty: Medium
Date: 2026-02-13

Description:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

This implementation uses the Divide and Conquer approach.

Function Description:
Complete the maxSubArray function with the following parameter:
    nums: List[int] - array of integers

Returns:
    int: the sum of the subarray with the largest sum

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Examples:

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Algorithm:
Divide and Conquer approach - O(n log n) time, O(log n) space

The maximum subarray can be in one of three places:
1. Entirely in the left half
2. Entirely in the right half
3. Crossing the middle point

We recursively solve for left and right halves, calculate the crossing sum,
and return the maximum of all three.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the maximum sum of a contiguous subarray using divide and conquer.

        Args:
            nums: Array of integers

        Returns:
            int: Maximum subarray sum
        """
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)
    print(f"Test 1: {nums} -> {result} (expected 6)")
    assert result == 6, f"Got: {result}"

    # Test case 2: single element
    nums = [1]
    result = solution.maxSubArray(nums)
    print(f"Test 2: {nums} -> {result} (expected 1)")
    assert result == 1, f"Got: {result}"

    # Test case 3
    nums = [5, 4, -1, 7, 8]
    result = solution.maxSubArray(nums)
    print(f"Test 3: {nums} -> {result} (expected 23)")
    assert result == 23, f"Got: {result}"

    # Test case 4: all negative
    nums = [-2, -1]
    result = solution.maxSubArray(nums)
    print(f"Test 4: {nums} -> {result} (expected -1)")
    assert result == -1, f"Got: {result}"

    # Test case 5: mix of positive and negative
    nums = [-2, 1]
    result = solution.maxSubArray(nums)
    print(f"Test 5: {nums} -> {result} (expected 1)")
    assert result == 1, f"Got: {result}"

    # Test case 6: larger array
    nums = [8, -19, 5, -4, 20]
    result = solution.maxSubArray(nums)
    print(f"Test 6: {nums} -> {result} (expected 21)")
    assert result == 21, f"Got: {result}"

    print("All tests passed!")
