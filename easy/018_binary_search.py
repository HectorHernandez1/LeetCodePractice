#!/bin/python3
"""
Problem: Binary Search
Source: LeetCode #704
Difficulty: Easy
Date: 2026-02-11

Description:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Function Description:
Complete the search function with the following parameters:
    nums: List[int] - sorted array of integers
    target: int - target value to search for

Returns:
    int: index of target if found, -1 otherwise

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.

Examples:

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search implementation.

        Args:
            nums: Sorted array of integers
            target: Target value to search for

        Returns:
            int: Index of target if found, -1 otherwise
        """
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1: target present
    nums = [-1, 0, 3, 5, 9, 12]
    result = solution.search(nums, 9)
    print(f"Test 1: {nums}, target = 9 -> {result} (expected 4)")
    assert result == 4, f"Got: {result}"

    # Test case 2: target absent
    nums = [-1, 0, 3, 5, 9, 12]
    result = solution.search(nums, 2)
    print(f"Test 2: {nums}, target = 2 -> {result} (expected -1)")
    assert result == -1, f"Got: {result}"

    # Test case 3: single element
    nums = [5]
    result = solution.search(nums, 5)
    print(f"Test 3: {nums}, target = 5 -> {result} (expected 0)")
    assert result == 0, f"Got: {result}"

    # Test case 4: first and last positions
    nums = [-1, 0, 3, 5, 9, 12]
    result = solution.search(nums, -1)
    print(f"Test 4: {nums}, target = -1 -> {result} (expected 0)")
    assert result == 0, f"Got: {result}"
    result = solution.search(nums, 12)
    print(f"Test 4b: {nums}, target = 12 -> {result} (expected 5)")
    assert result == 5, f"Got: {result}"

    print("All tests passed!")
