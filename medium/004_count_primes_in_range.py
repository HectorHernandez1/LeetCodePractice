#!/bin/python3
"""
Problem: Count Primes in Range
Source: Classic
Difficulty: Medium
Date: 2026-02-13

Description:
Given two integers `left` and `right`, return the number of prime numbers
that exist between `left` and `right` (inclusive).

A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Function Description:
Complete the countPrimesInRange function with the following parameters:
    left: int - the lower bound of the range (inclusive)
    right: int - the upper bound of the range (inclusive)

Returns:
    int: the count of prime numbers in the range [left, right]

Constraints:
- 1 <= left <= right <= 10^6

Examples:

Example 1:
Input: left = 1, right = 10
Output: 4
Explanation: The primes between 1 and 10 are [2, 3, 5, 7].

Example 2:
Input: left = 10, right = 20
Output: 4
Explanation: The primes between 10 and 20 are [11, 13, 17, 19].

Example 3:
Input: left = 1, right = 1
Output: 0
Explanation: 1 is not a prime number.

Example 4:
Input: left = 14, right = 16
Output: 0
Explanation: 14, 15, and 16 are all composite numbers.

Example 5:
Input: left = 2, right = 2
Output: 1
Explanation: 2 is the smallest prime number.

Note:
This problem can be solved using:
1. Trial Division - check each number individually: O((right - left) * sqrt(right))
2. Sieve of Eratosthenes - precompute all primes up to right: O(right * log(log(right)))
Try the Sieve approach for better performance on large ranges!
"""


class Solution:
    def countPrimesInRange(self, left: int, right: int) -> int:
        """
        Count the number of prime numbers in the range [left, right].

        Args:
            left: Lower bound of the range (inclusive)
            right: Upper bound of the range (inclusive)

        Returns:
            int: Number of primes in the range
        """
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    left, right = 1, 10
    result = solution.countPrimesInRange(left, right)
    print(f"Input: left = {left}, right = {right}")
    print(f"Output: {result}")
    print(f"Expected: 4")
    print()

    # Test case 2
    print("Test 2:")
    left, right = 10, 20
    result = solution.countPrimesInRange(left, right)
    print(f"Input: left = {left}, right = {right}")
    print(f"Output: {result}")
    print(f"Expected: 4")
    print()

    # Test case 3
    print("Test 3:")
    left, right = 1, 1
    result = solution.countPrimesInRange(left, right)
    print(f"Input: left = {left}, right = {right}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print()

    # Test case 4
    print("Test 4:")
    left, right = 14, 16
    result = solution.countPrimesInRange(left, right)
    print(f"Input: left = {left}, right = {right}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print()

    # Test case 5
    print("Test 5:")
    left, right = 2, 2
    result = solution.countPrimesInRange(left, right)
    print(f"Input: left = {left}, right = {right}")
    print(f"Output: {result}")
    print(f"Expected: 1")
    print()
