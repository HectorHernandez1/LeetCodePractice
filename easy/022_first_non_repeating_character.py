#!/bin/python3
"""
Problem: First Unique Character in a String
Source: LeetCode #387
Difficulty: Easy
Date: 2026-02-13

Description:
Given a list of characters, return the first character that does not repeat
in the list. If every character repeats, return an empty string "".

Function Description:
Complete the firstNonRepeatingChar function with the following parameters:
    chars: List[str] - list of single characters

Returns:
    str: The first non-repeating character, or "" if none exists

Constraints:
- 1 <= len(chars) <= 10^5
- chars[i] is a lowercase English letter

Examples:

Example 1:
Input: chars = ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']
Output: 'l'
Explanation: 'l' is the first character that appears only once.

Example 2:
Input: chars = ['a', 'a', 'b', 'b']
Output: ''
Explanation: Every character repeats, so return "".

Example 3:
Input: chars = ['a', 'b', 'c', 'a', 'b']
Output: 'c'
Explanation: 'c' is the only character that does not repeat.

Example 4:
Input: chars = ['z']
Output: 'z'
Explanation: Only one character, so it is non-repeating.
"""

from typing import List


class Solution:
    def firstNonRepeatingChar(self, chars: List[str]) -> str:
        """
        Find the first non-repeating character in a list of characters.

        Args:
            chars: List of single characters

        Returns:
            str: The first non-repeating character, or "" if none exists
        """
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    chars = ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']
    result = solution.firstNonRepeatingChar(chars)
    print(f"Input: chars = {chars}")
    print(f"Output: '{result}'")
    print(f"Expected: 'l'")
    print()

    # Test case 2
    print("Test 2:")
    chars = ['a', 'a', 'b', 'b']
    result = solution.firstNonRepeatingChar(chars)
    print(f"Input: chars = {chars}")
    print(f"Output: '{result}'")
    print(f"Expected: ''")
    print()

    # Test case 3
    print("Test 3:")
    chars = ['a', 'b', 'c', 'a', 'b']
    result = solution.firstNonRepeatingChar(chars)
    print(f"Input: chars = {chars}")
    print(f"Output: '{result}'")
    print(f"Expected: 'c'")
    print()

    # Test case 4
    print("Test 4:")
    chars = ['z']
    result = solution.firstNonRepeatingChar(chars)
    print(f"Input: chars = {chars}")
    print(f"Output: '{result}'")
    print(f"Expected: 'z'")
    print()
