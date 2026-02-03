/*
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
    nums1: number[] - first sorted array with extra space
    m: number - number of initialized elements in nums1
    nums2: number[] - second sorted array
    n: number - number of elements in nums2

Returns:
    void: Modifies nums1 in-place

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
*/

class Solution {
    merge(nums1: number[], m: number, nums2: number[], n: number): void {
        /**
         * Merge two sorted arrays in-place using two-pointer technique.
         *
         * Args:
         *     nums1: First sorted array with extra space
         *     m: Number of initialized elements in nums1
         *     nums2: Second sorted array
         *     n: Number of elements in nums2
         *
         * Returns:
         *     void: Modifies nums1 in-place
         */
        // Write your code here
    }
}

// Test cases
function runTests(): void {
    const solution = new Solution();

    // Test case 1
    console.log("Test 1:");
    const nums1_1: number[] = [1, 2, 3, 0, 0, 0];
    const m1: number = 3;
    const nums2_1: number[] = [2, 5, 6];
    const n1: number = 3;
    console.log(
        `Input: nums1 = ${JSON.stringify(nums1_1)}, m = ${m1}, nums2 = ${JSON.stringify(nums2_1)}, n = ${n1}`
    );
    solution.merge(nums1_1, m1, nums2_1, n1);
    console.log(`Output: ${JSON.stringify(nums1_1)}`);
    console.log(`Expected: [1, 2, 2, 3, 5, 6]`);
    console.log();

    // Test case 2
    console.log("Test 2:");
    const nums1_2: number[] = [1];
    const m2: number = 1;
    const nums2_2: number[] = [];
    const n2: number = 0;
    console.log(
        `Input: nums1 = ${JSON.stringify(nums1_2)}, m = ${m2}, nums2 = ${JSON.stringify(nums2_2)}, n = ${n2}`
    );
    solution.merge(nums1_2, m2, nums2_2, n2);
    console.log(`Output: ${JSON.stringify(nums1_2)}`);
    console.log(`Expected: [1]`);
    console.log();

    // Test case 3
    console.log("Test 3:");
    const nums1_3: number[] = [0];
    const m3: number = 0;
    const nums2_3: number[] = [1];
    const n3: number = 1;
    console.log(
        `Input: nums1 = ${JSON.stringify(nums1_3)}, m = ${m3}, nums2 = ${JSON.stringify(nums2_3)}, n = ${n3}`
    );
    solution.merge(nums1_3, m3, nums2_3, n3);
    console.log(`Output: ${JSON.stringify(nums1_3)}`);
    console.log(`Expected: [1]`);
    console.log();
}

// Run tests if this file is executed directly
runTests();
