#!/bin/python3
"""
Problem: Merge Sorted Array
Source: LeetCode #88
Difficulty: Easy
Date: TBD

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.

Function Description:
Complete the merge function with the following parameters:
    nums1: List[int] - first sorted array with extra space
    m: int - number of initialized elements in nums1
    nums2: List[int] - second sorted array
    n: int - number of elements in nums2

Returns:
    None: Modifies nums1 in-place

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

Follow-up: Can you come up with an algorithm that runs in O(m + n) time?

Examples:

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays in-place using two-pointer technique.

        Args:
            nums1: First sorted array with extra space
            m: Number of initialized elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2

        Returns:
            None: Modifies nums1 in-place
        """
        # Write your code here
        #base case
        if not nums2:
            return
        j = 0
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j+=1
        nums1.sort()

# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"Input: nums1 = {nums1[:m] + [0]*n}, m = {m}, nums2 = {nums2}, n = {n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    print(f"Expected: [1, 2, 2, 3, 5, 6]")
    print()

    # Test case 2
    print("Test 2:")
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(f"Input: nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    print(f"Expected: [1]")
    print()

    # Test case 3
    print("Test 3:")
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(f"Input: nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}")
    solution.merge(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    print(f"Expected: [1]")
    print()
