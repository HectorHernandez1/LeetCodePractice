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
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1: odd length
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(f"Test 1: -> {s} (expected ['o', 'l', 'l', 'e', 'h'])")
    assert s == ["o", "l", "l", "e", "h"], f"Got: {s}"

    # Test case 2: even length
    s = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s)
    print(f"Test 2: -> {s} (expected ['h', 'a', 'n', 'n', 'a', 'H'])")
    assert s == ["h", "a", "n", "n", "a", "H"], f"Got: {s}"

    # Test case 3: single character
    s = ["a"]
    solution.reverseString(s)
    print(f"Test 3: -> {s} (expected ['a'])")
    assert s == ["a"], f"Got: {s}"

    # Test case 4: two characters
    s = ["A", "b"]
    solution.reverseString(s)
    print(f"Test 4: -> {s} (expected ['b', 'A'])")
    assert s == ["b", "A"], f"Got: {s}"

    print("All tests passed!")
