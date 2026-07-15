#!/bin/python3
"""
Problem: Two Sum
Source: LeetCode #1
Difficulty: Easy
Date: 2026-01-20

Description:
Given an array of integers nums and an integer target, return the indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order.

Function Description:
Complete the twoSum function with the following parameters:
    nums: List[int] - array of integers
    target: int - target sum

Returns:
    List[int]: indices of the two numbers that add up to target

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

Examples:

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target.

        Args:
            nums: Array of integers
            target: Target sum

        Returns:
            List of two indices where nums[i] + nums[j] == target
        """
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    def check(nums, target, expected):
        """Assert indices match (order-independent) and actually sum to target."""
        result = solution.twoSum(nums, target)
        print(f"nums = {nums}, target = {target} -> {result} (expected {expected})")
        assert result is not None, "Got: None"
        assert sorted(result) == sorted(expected), f"Got: {result}"
        assert nums[result[0]] + nums[result[1]] == target

    print("Test 1: ", end='')
    check([2, 7, 11, 15], 9, [0, 1])

    print("Test 2: ", end='')
    check([3, 2, 4], 6, [1, 2])

    print("Test 3: duplicate values, ", end='')
    check([3, 3], 6, [0, 1])

    print("Test 4: negative numbers, ", end='')
    check([-1, -2, -3, 5, 10], 8, [3, 4])

    print("Test 5: ", end='')
    check([1, 2, 3, 4, 5], 9, [3, 4])

    print("All tests passed!")
