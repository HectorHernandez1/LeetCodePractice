#!/bin/python3
"""
Problem: Time Conversion
Source: HackerRank
Difficulty: Easy
Date: 2026-01-14

Description:
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Function Description:
Complete the timeConversion function with the following parameter(s):
    s: a time in 12-hour format

Returns:
    string: the time in 24-hour format

Input Format:
A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints:
- All input times are valid

Sample Input:
07:05:45PM

Sample Output:
19:05:45
"""

import math
import os
import random
import re
import sys

def timeConversion(s):
    """
    Convert time from 12-hour AM/PM format to 24-hour military time.

    Args:
        s: a time string in 12-hour format (e.g., "07:05:45PM")

    Returns:
        string: the time in 24-hour format (e.g., "19:05:45")
    """
    # Write your code here
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    s1 = "07:05:45PM"
    print(f"Input: {s1}")
    print(f"Output: {timeConversion(s1)}")
    # Expected output: 19:05:45
    print()

    # Test case 2
    print("Test 2:")
    s2 = "12:01:00PM"
    print(f"Input: {s2}")
    print(f"Output: {timeConversion(s2)}")
    # Expected output: 12:01:00
    print()

    # Test case 3
    print("Test 3:")
    s3 = "12:01:00AM"
    print(f"Input: {s3}")
    print(f"Output: {timeConversion(s3)}")
    # Expected output: 00:01:00
    print()

    # Test case 4
    print("Test 4:")
    s4 = "12:00:00AM"
    print(f"Input: {s4}")
    print(f"Output: {timeConversion(s4)}")
    # Expected output: 00:00:00
    print()

    # Test case 5
    print("Test 5:")
    s5 = "12:00:00PM"
    print(f"Input: {s5}")
    print(f"Output: {timeConversion(s5)}")
    # Expected output: 12:00:00
