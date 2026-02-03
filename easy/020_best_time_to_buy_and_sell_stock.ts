/*
Problem: Best Time to Buy and Sell Stock
Source: LeetCode #121
Difficulty: Easy
Date: TBD

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Function Description:
Complete the maxProfit function with the following parameters:
    prices: number[] - array of stock prices

Returns:
    number: maximum profit achievable

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Examples:

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
*/

class Solution {
    maxProfit(prices: number[]): number {
        /**
         * Find maximum profit from buying and selling stock once.
         *
         * Args:
         *     prices: Array of stock prices
         *
         * Returns:
         *     number: Maximum profit achievable
         */
        // Write your code here
        return 0;
    }
}

// Test cases
function runTests(): void {
    const solution = new Solution();

    // Test case 1
    console.log("Test 1:");
    const prices1: number[] = [7, 1, 5, 3, 6, 4];
    const result1: number = solution.maxProfit(prices1);
    console.log(`Input: prices = ${JSON.stringify(prices1)}`);
    console.log(`Output: ${result1}`);
    console.log(`Expected: 5`);
    console.log();

    // Test case 2
    console.log("Test 2:");
    const prices2: number[] = [7, 6, 4, 3, 1];
    const result2: number = solution.maxProfit(prices2);
    console.log(`Input: prices = ${JSON.stringify(prices2)}`);
    console.log(`Output: ${result2}`);
    console.log(`Expected: 0`);
    console.log();

    // Test case 3
    console.log("Test 3:");
    const prices3: number[] = [2, 4, 1];
    const result3: number = solution.maxProfit(prices3);
    console.log(`Input: prices = ${JSON.stringify(prices3)}`);
    console.log(`Output: ${result3}`);
    console.log(`Expected: 2`);
    console.log();
}

// Run tests if this file is executed directly
runTests();
