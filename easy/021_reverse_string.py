#!/bin/python3
"""
Problem: Reverse String
Source: LeetCode #344
Difficulty: Easy
Date: TBD

Description:
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Function Description:
Complete the reverseString function with the following parameter:
    s: List[str] - array of characters

Returns:
    None: Modifies s in-place

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character.

Examples:

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse a string in-place.

        Args:
            s: Array of characters

        Returns:
            None: Modifies s in-place
        """
        # Write your code here
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    s = ["h", "e", "l", "l", "o"]
    print(f"Input: s = {s}")
    solution.reverseString(s)
    print(f"Output: {s}")
    print(f"Expected: ['o', 'l', 'l', 'e', 'h']")
    print()

    # Test case 2
    print("Test 2:")
    s = ["H", "a", "n", "n", "a", "h"]
    print(f"Input: s = {s}")
    solution.reverseString(s)
    print(f"Output: {s}")
    print(f"Expected: ['h', 'a', 'n', 'n', 'a', 'H']")
    print()

    # Test case 3: Single character
    print("Test 3:")
    s = ["a"]
    print(f"Input: s = {s}")
    solution.reverseString(s)
    print(f"Output: {s}")
    print(f"Expected: ['a']")
    print()

    # Test case 4: Two characters
    print("Test 4:")
    s = ["A", "b"]
    print(f"Input: s = {s}")
    solution.reverseString(s)
    print(f"Output: {s}")
    print(f"Expected: ['b', 'A']")
    print()
