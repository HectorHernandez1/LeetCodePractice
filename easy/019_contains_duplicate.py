#!/bin/python3
"""
Problem: Contains Duplicate
Source: LeetCode #217
Difficulty: Easy
Date: TBD

Description:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Function Description:
Complete the containsDuplicate function with the following parameters:
    nums: List[int] - array of integers

Returns:
    bool: True if any value appears twice, False otherwise

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Examples:

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if array contains duplicates using a hash set.

        Args:
            nums: Array of integers

        Returns:
            bool: True if duplicates exist, False otherwise
        """
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2
    print("Test 2:")
    nums = [1, 2, 3, 4]
    result = solution.containsDuplicate(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()

    # Test case 3
    print("Test 3:")
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = solution.containsDuplicate(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()
