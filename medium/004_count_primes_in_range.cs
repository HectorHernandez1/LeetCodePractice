/*
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
Complete the CountPrimesInRange function with the following parameters:
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
*/

using System;

public class Solution
{
    /// <summary>
    /// Count the number of prime numbers in the range [left, right].
    /// </summary>
    /// <param name="left">Lower bound of the range (inclusive)</param>
    /// <param name="right">Upper bound of the range (inclusive)</param>
    /// <returns>Number of primes in the range</returns>
    public int CountPrimesInRange(int left, int right)
    {
        // Write your code here
        return 0;
    }
}

// Test cases
public class Program
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();

        // Test case 1
        Console.WriteLine("Test 1:");
        int result = solution.CountPrimesInRange(1, 10);
        Console.WriteLine($"Input: left = 1, right = 10");
        Console.WriteLine($"Output: {result}");
        Console.WriteLine($"Expected: 4");
        Console.WriteLine();

        // Test case 2
        Console.WriteLine("Test 2:");
        result = solution.CountPrimesInRange(10, 20);
        Console.WriteLine($"Input: left = 10, right = 20");
        Console.WriteLine($"Output: {result}");
        Console.WriteLine($"Expected: 4");
        Console.WriteLine();

        // Test case 3
        Console.WriteLine("Test 3:");
        result = solution.CountPrimesInRange(1, 1);
        Console.WriteLine($"Input: left = 1, right = 1");
        Console.WriteLine($"Output: {result}");
        Console.WriteLine($"Expected: 0");
        Console.WriteLine();

        // Test case 4
        Console.WriteLine("Test 4:");
        result = solution.CountPrimesInRange(14, 16);
        Console.WriteLine($"Input: left = 14, right = 16");
        Console.WriteLine($"Output: {result}");
        Console.WriteLine($"Expected: 0");
        Console.WriteLine();

        // Test case 5
        Console.WriteLine("Test 5:");
        result = solution.CountPrimesInRange(2, 2);
        Console.WriteLine($"Input: left = 2, right = 2");
        Console.WriteLine($"Output: {result}");
        Console.WriteLine($"Expected: 1");
        Console.WriteLine();
    }
}
