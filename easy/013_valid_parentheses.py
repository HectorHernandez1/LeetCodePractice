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
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    s = "()"
    result = solution.isValid(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2
    print("Test 2:")
    s = "()[]{}"
    result = solution.isValid(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 3
    print("Test 3:")
    s = "(]"
    result = solution.isValid(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()

    # Test case 4
    print("Test 4:")
    s = "([)]"
    result = solution.isValid(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()

    # Test case 5
    print("Test 5:")
    s = "{[]}"
    result = solution.isValid(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()
