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
        def divideConquer(left: int, right: int) -> int:
            """
            Recursively find max subarray sum in range [left, right].

            Args:
                left: Left boundary index
                right: Right boundary index

            Returns:
                int: Maximum subarray sum in this range
            """
            # Base case: only one element
            if left == right:
                return nums[left]

            # Find the middle point
            mid = (left + right) // 2

            # Recursively find max in left and right halves
            left_max = divideConquer(left, mid)
            right_max = divideConquer(mid + 1, right)

            # Find max crossing subarray
            cross_max = maxCrossingSum(left, mid, right)

            # Return the maximum of all three
            return max(left_max, right_max, cross_max)

        def maxCrossingSum(left: int, mid: int, right: int) -> int:
            """
            Find maximum sum of subarray that crosses the midpoint.

            Args:
                left: Left boundary index
                mid: Middle index
                right: Right boundary index

            Returns:
                int: Maximum crossing subarray sum
            """
            # Find max sum starting from mid and going left
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left - 1, -1):  # Go backwards from mid
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)

            # Find max sum starting from mid+1 and going right
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):  # Go forwards from mid+1
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)

            # The crossing max is both sides combined
            return left_sum + right_sum

        return divideConquer(0, len(nums) - 1)


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: 6")
    print(f"Pass: {result == 6}")
    print()

    # Test case 2
    print("Test 2:")
    nums = [1]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: 1")
    print(f"Pass: {result == 1}")
    print()

    # Test case 3
    print("Test 3:")
    nums = [5, 4, -1, 7, 8]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: 23")
    print(f"Pass: {result == 23}")
    print()

    # Test case 4 (all negative)
    print("Test 4:")
    nums = [-2, -1]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: -1")
    print(f"Pass: {result == -1}")
    print()

    # Test case 5 (mix of positive and negative)
    print("Test 5:")
    nums = [-2, 1]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: 1")
    print(f"Pass: {result == 1}")
    print()

    # Test case 6 (larger array)
    print("Test 6:")
    nums = [8, -19, 5, -4, 20]
    result = solution.maxSubArray(nums)
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: 21")
    print(f"Pass: {result == 21}")
    print()
