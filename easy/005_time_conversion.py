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
    pass
        


# Test cases
if __name__ == '__main__':
    # Test case 1
    s = "07:05:45PM"
    result = timeConversion(s)
    print(f"Test 1: {s} -> {result} (expected 19:05:45)")
    assert result == "19:05:45", f"Got: {result!r}"

    # Test case 2: noon stays 12
    s = "12:01:00PM"
    result = timeConversion(s)
    print(f"Test 2: {s} -> {result} (expected 12:01:00)")
    assert result == "12:01:00", f"Got: {result!r}"

    # Test case 3: midnight becomes 00
    s = "12:01:00AM"
    result = timeConversion(s)
    print(f"Test 3: {s} -> {result} (expected 00:01:00)")
    assert result == "00:01:00", f"Got: {result!r}"

    # Test case 4: exactly midnight
    s = "12:00:00AM"
    result = timeConversion(s)
    print(f"Test 4: {s} -> {result} (expected 00:00:00)")
    assert result == "00:00:00", f"Got: {result!r}"

    # Test case 5: exactly noon
    s = "12:00:00PM"
    result = timeConversion(s)
    print(f"Test 5: {s} -> {result} (expected 12:00:00)")
    assert result == "12:00:00", f"Got: {result!r}"

    print("All tests passed!")
