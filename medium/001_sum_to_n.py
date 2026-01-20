#!/bin/python3
"""
Problem: Sum to N
Source: Classic Algorithm Problem
Difficulty: Easy/Medium
Date: 2026-01-19

Description:
Given a list of integers and a target integer n, write a function called sum_to_n
that finds all combinations of numbers from the list that sum to the value n.

Each number in the list may only be used once in a combination.
The solution set must not contain duplicate combinations.

Function Description:
Complete the sum_to_n function with the following parameters:
    nums: a list of integers
    n: the target sum

Returns:
    List[List[int]]: a list of all combinations that sum to n

Example 1:
Input: nums = [2, 3, 5, 7, 10], n = 10
Output: [[3, 7], [10], [2, 3, 5]]
Explanation:
    - 3 + 7 = 10
    - 10 = 10
    - 2 + 3 + 5 = 10

Example 2:
Input: nums = [1, 2, 3, 4, 5], n = 5
Output: [[1, 4], [2, 3], [5]]
Explanation:
    - 1 + 4 = 5
    - 2 + 3 = 5
    - 5 = 5

Example 3:
Input: nums = [1, 1, 2, 3], n = 4
Output: [[1, 1, 2], [1, 3]]
Explanation:
    - 1 + 1 + 2 = 4
    - 1 + 3 = 4

Constraints:
- 1 <= len(nums) <= 20
- 1 <= nums[i] <= 50
- 1 <= n <= 100

Hint:
Think about using recursion/backtracking. At each step, you have a choice:
include the current number in your combination or skip it.
"""


def sum_to_n(nums, n):
    """
    Find all combinations of numbers that sum to n.

    Args:
        nums: list of integers to choose from
        n: target sum

    Returns:
        List[List[int]]: all combinations that sum to n
    """
    results = []

    # needs access to nums and 
    def backtrack(start, current_combo, remaining):
        # base case -
        # SUCCESS: we hit exactly the target
        if remaining == 0:
            results.append(current_combo.copy())
            return
        # FAILURE: overshot or no more numbers
        if remaining < 0:
            return

        for i in range(start, len(nums)):
            # choose: add this number
            current_combo.append(nums[i])

            #explore: recurse ()
            backtrack(i+1,current_combo,remaining-nums[i])

            #unchoose: remove it (backtrack)
            current_combo.pop()

    # start at index 0, empty combo, full target
    backtrack(0, [], n)

    return results



        



# Test cases
if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [2, 3, 5, 7, 10]
    n1 = 10
    print(f"nums = {nums1}, n = {n1}")
    result1 = sum_to_n(nums1, n1)
    print(f"Output: {result1}")
    # Expected: [[2, 3, 5], [3, 7], [10]] (order may vary)
    print()

    # Test case 2
    print("Test 2:")
    nums2 = [1, 2, 3, 4, 5]
    n2 = 5
    print(f"nums = {nums2}, n = {n2}")
    result2 = sum_to_n(nums2, n2)
    print(f"Output: {result2}")
    # Expected: [[1, 4], [2, 3], [5]] (order may vary)
    print()

    # Test case 3: With duplicates in input
    print("Test 3:")
    nums3 = [1, 1, 2, 3]
    n3 = 4
    print(f"nums = {nums3}, n = {n3}")
    result3 = sum_to_n(nums3, n3)
    print(f"Output: {result3}")
    # Expected: [[1, 1, 2], [1, 3]] (order may vary)
    print()

    # Test case 4: No solution
    print("Test 4:")
    nums4 = [5, 10, 15]
    n4 = 3
    print(f"nums = {nums4}, n = {n4}")
    result4 = sum_to_n(nums4, n4)
    print(f"Output: {result4}")
    # Expected: []
    print()

    # Test case 5: Single element solution
    print("Test 5:")
    nums5 = [7]
    n5 = 7
    print(f"nums = {nums5}, n = {n5}")
    result5 = sum_to_n(nums5, n5)
    print(f"Output: {result5}")
    # Expected: [[7]]
