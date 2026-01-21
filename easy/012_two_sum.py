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
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1: [2,7,11,15], target = 9
    print("Test 1:")
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()

    # Test case 2: [3,2,4], target = 6
    print("Test 2:")
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [1, 2]")
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()

    # Test case 3: [3,3], target = 6
    print("Test 3:")
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()

    # Test case 4: Negative numbers
    print("Test 4:")
    nums = [-1, -2, -3, 5, 10]
    target = 8
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [3, 4]")
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()

    # Test case 5: Duplicate values
    print("Test 5:")
    nums = [1, 2, 3, 4, 5]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [3, 4]")
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
