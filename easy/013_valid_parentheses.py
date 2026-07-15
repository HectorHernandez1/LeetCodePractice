#!/bin/python3
"""
Problem: Valid Parentheses
Source: LeetCode #20
Difficulty: Easy
Date: TBD

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Function Description:
Complete the isValid function with the following parameters:
    s: str - string containing only brackets

Returns:
    bool: True if the string is valid, False otherwise

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Examples:

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if brackets are balanced using a stack.

        Args:
            s: String containing only brackets

        Returns:
            bool: True if valid, False otherwise
        """
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    s = "()"
    result = solution.isValid(s)
    print(f"Test 1: '{s}' -> {result} (expected True)")
    assert result == True

    # Test case 2
    s = "()[]{}"
    result = solution.isValid(s)
    print(f"Test 2: '{s}' -> {result} (expected True)")
    assert result == True

    # Test case 3: mismatched pair
    s = "(]"
    result = solution.isValid(s)
    print(f"Test 3: '{s}' -> {result} (expected False)")
    assert result == False

    # Test case 4: interleaved brackets
    s = "([)]"
    result = solution.isValid(s)
    print(f"Test 4: '{s}' -> {result} (expected False)")
    assert result == False

    # Test case 5: nested brackets
    s = "{[]}"
    result = solution.isValid(s)
    print(f"Test 5: '{s}' -> {result} (expected True)")
    assert result == True

    # Test case 6: unclosed opening bracket
    s = "("
    result = solution.isValid(s)
    print(f"Test 6: '{s}' -> {result} (expected False)")
    assert result == False

    print("All tests passed!")
