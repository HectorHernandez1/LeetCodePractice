#!/bin/python3
"""
Problem: Valid Palindrome
Source: LeetCode #125
Difficulty: Easy
Date: TBD

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Function Description:
Complete the isPalindrome function with the following parameters:
    s: str - input string

Returns:
    bool: True if the string is a palindrome, False otherwise

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Examples:

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome using two-pointer technique.

        Args:
            s: Input string

        Returns:
            bool: True if palindrome, False otherwise
        """
        # Write your code here
        pass


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    s = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2
    print("Test 2:")
    s = "race a car"
    result = solution.isPalindrome(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()

    # Test case 3
    print("Test 3:")
    s = " "
    result = solution.isPalindrome(s)
    print(f"Input: s = '{s}'")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()
