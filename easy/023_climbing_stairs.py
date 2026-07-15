#!/bin/python3
"""
Problem: Climbing Stairs
Source: LeetCode #70
Difficulty: Easy
Date: TBD

Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Function Description:
Complete the climbStairs function with the following parameters:
    n: int - number of steps to reach the top

Returns:
    int: number of distinct ways to climb to the top

Constraints:
- 1 <= n <= 45

Examples:

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Count distinct ways to climb n stairs taking 1 or 2 steps at a time.

        Hint: the number of ways to reach step n is the number of ways to
        reach step (n-1) plus the number of ways to reach step (n-2).

        Args:
            n: Number of steps to reach the top

        Returns:
            int: Number of distinct ways to climb to the top
        """
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    n = 2
    result = solution.climbStairs(n)
    print(f"Test 1: n = {n} -> {result} (expected 2)")
    assert result == 2

    # Test case 2
    n = 3
    result = solution.climbStairs(n)
    print(f"Test 2: n = {n} -> {result} (expected 3)")
    assert result == 3

    # Test case 3: smallest input
    n = 1
    result = solution.climbStairs(n)
    print(f"Test 3: n = {n} -> {result} (expected 1)")
    assert result == 1

    # Test case 4: Fibonacci sanity check
    n = 5
    result = solution.climbStairs(n)
    print(f"Test 4: n = {n} -> {result} (expected 8)")
    assert result == 8

    # Test case 5: largest input per constraints
    n = 45
    result = solution.climbStairs(n)
    print(f"Test 5: n = {n} -> {result} (expected 1836311903)")
    assert result == 1836311903

    print("All tests passed!")
