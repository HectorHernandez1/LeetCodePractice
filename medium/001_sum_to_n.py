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
    pass


# Test cases
if __name__ == '__main__':
    def canonical(combos):
        """Sort each combination and the list of combinations so
        assertions are independent of the order the solution returns."""
        assert combos is not None, "Got: None"
        return sorted(sorted(c) for c in combos)

    # Test case 1
    nums, n = [2, 3, 5, 7, 10], 10
    result = sum_to_n(nums, n)
    expected = [[2, 3, 5], [3, 7], [10]]
    print(f"Test 1: nums = {nums}, n = {n} -> {result}")
    assert canonical(result) == canonical(expected), f"Got: {result}"

    # Test case 2
    nums, n = [1, 2, 3, 4, 5], 5
    result = sum_to_n(nums, n)
    expected = [[1, 4], [2, 3], [5]]
    print(f"Test 2: nums = {nums}, n = {n} -> {result}")
    assert canonical(result) == canonical(expected), f"Got: {result}"

    # Test case 3: duplicates in input
    nums, n = [1, 1, 2, 3], 4
    result = sum_to_n(nums, n)
    expected = [[1, 1, 2], [1, 3]]
    print(f"Test 3: nums = {nums}, n = {n} -> {result}")
    assert canonical(result) == canonical(expected), f"Got: {result}"

    # Test case 4: no solution
    nums, n = [5, 10, 15], 3
    result = sum_to_n(nums, n)
    print(f"Test 4: nums = {nums}, n = {n} -> {result} (expected [])")
    assert result == [], f"Got: {result}"

    # Test case 5: single element solution
    nums, n = [7], 7
    result = sum_to_n(nums, n)
    print(f"Test 5: nums = {nums}, n = {n} -> {result} (expected [[7]])")
    assert canonical(result) == [[7]], f"Got: {result}"

    print("All tests passed!")
