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
Complete the countPrimesInRange function with the following parameters:
    left: number - the lower bound of the range (inclusive)
    right: number - the upper bound of the range (inclusive)

Returns:
    number: the count of prime numbers in the range [left, right]

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

class Solution {
    /**
     * Count the number of prime numbers in the range [left, right].
     *
     * @param {number} left - Lower bound of the range (inclusive)
     * @param {number} right - Upper bound of the range (inclusive)
     * @returns {number} Number of primes in the range
     */
    countPrimesInRange(left, right) {
        // Write your code here
        return 0;
    }
}

// Test cases
function runTests() {
    const solution = new Solution();

    // Test case 1
    console.log("Test 1:");
    let result = solution.countPrimesInRange(1, 10);
    console.log(`Input: left = 1, right = 10`);
    console.log(`Output: ${result}`);
    console.log(`Expected: 4`);
    console.log();

    // Test case 2
    console.log("Test 2:");
    result = solution.countPrimesInRange(10, 20);
    console.log(`Input: left = 10, right = 20`);
    console.log(`Output: ${result}`);
    console.log(`Expected: 4`);
    console.log();

    // Test case 3
    console.log("Test 3:");
    result = solution.countPrimesInRange(1, 1);
    console.log(`Input: left = 1, right = 1`);
    console.log(`Output: ${result}`);
    console.log(`Expected: 0`);
    console.log();

    // Test case 4
    console.log("Test 4:");
    result = solution.countPrimesInRange(14, 16);
    console.log(`Input: left = 14, right = 16`);
    console.log(`Output: ${result}`);
    console.log(`Expected: 0`);
    console.log();

    // Test case 5
    console.log("Test 5:");
    result = solution.countPrimesInRange(2, 2);
    console.log(`Input: left = 2, right = 2`);
    console.log(`Output: ${result}`);
    console.log(`Expected: 1`);
    console.log();
}

// Run tests if this file is executed directly
runTests();
