#!/bin/python3
"""
Problem: Moving Average
Difficulty: Medium
Date: TBD

Description:
Calculate the moving average of a list of values with a given window size.

Args:
    values: List of numeric values
    window_size: Size of the moving window

Returns:
    List of moving averages. The first (window_size - 1) elements should be None
    since we don't have enough data points.

Example:
    Input: values = [1, 2, 3, 4, 5, 6], window_size = 3
    Output: [None, None, 2.0, 3.0, 4.0, 5.0]

    Explanation:
    - Index 0-1: Not enough data (need 3 points)
    - Index 2: avg(1,2,3) = 2.0
    - Index 3: avg(2,3,4) = 3.0
    - Index 4: avg(3,4,5) = 4.0
    - Index 5: avg(4,5,6) = 5.0

Time Complexity: O(n) with sliding window approach
Space Complexity: O(n) for result list

Hint: Use a sliding window approach for O(n) time complexity.
Don't recalculate the sum for each window - subtract the left element and add the right element.
"""


def calculate_moving_average(values, window_size):
    """
    Calculate the moving average with a sliding window.

    Args:
        values: List of numeric values
        window_size: Size of the moving window

    Returns:
        List of moving averages
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: Moving average with window size 3")
    values = [1, 2, 3, 4, 5, 6]
    window_size = 3

    result = calculate_moving_average(values, window_size)
    expected = [None, None, 2.0, 3.0, 4.0, 5.0]
    print(f"Input: values = {values}, window_size = {window_size}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("PASS" if result == expected else f"FAIL")
    print()

    print("Test 2: Moving average with window size 1")
    result2 = calculate_moving_average([1, 2, 3], 1)
    expected2 = [1.0, 2.0, 3.0]
    print(f"Input: values = [1, 2, 3], window_size = 1")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print("PASS" if result2 == expected2 else f"FAIL")
