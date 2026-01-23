#!/bin/python3
"""
Problem: Time Series Analysis
Difficulty: Medium
Date: TBD

Description:
Find all sensors where the temperature increased for N consecutive readings.

Args:
    readings: List of dicts with keys: sensor_id, temp, hour
    consecutive_count: Number of consecutive increases to look for (default: 3)

Returns:
    List of sensor_ids that had N consecutive temperature increases

Example:
    Input:
    [
        {"sensor_id": 1, "temp": 70, "hour": 1},
        {"sensor_id": 1, "temp": 72, "hour": 2},
        {"sensor_id": 1, "temp": 75, "hour": 3},
        {"sensor_id": 1, "temp": 74, "hour": 4},
        {"sensor_id": 2, "temp": 65, "hour": 1},
        {"sensor_id": 2, "temp": 66, "hour": 2},
        {"sensor_id": 2, "temp": 67, "hour": 3},
    ]

    Output:
    [1, 2]

Note: Sensor 1 had 3 consecutive increases (70->72->75), then decreased.
      Sensor 2 had 3 consecutive increases (65->66->67).

Time Complexity: O(n log n) for sorting + O(n) for scanning = O(n log n)
Space Complexity: O(n) for storing grouped readings

Hints:
1. Group readings by sensor_id
2. Sort each sensor's readings by hour
3. For each sensor, check for consecutive increases
4. Track consecutive increase count as you iterate
"""


def find_consecutive_increases(readings, consecutive_count=3):
    """
    Find sensors with N consecutive temperature increases.

    Args:
        readings: List of dicts with keys: sensor_id, temp, hour
        consecutive_count: Number of consecutive increases to look for (default: 3)

    Returns:
        List of sensor_ids that had N consecutive temperature increases
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: Find sensors with 3 consecutive increases")
    readings = [
        {"sensor_id": 1, "temp": 70, "hour": 1},
        {"sensor_id": 1, "temp": 72, "hour": 2},
        {"sensor_id": 1, "temp": 75, "hour": 3},
        {"sensor_id": 1, "temp": 74, "hour": 4},
        {"sensor_id": 2, "temp": 65, "hour": 1},
        {"sensor_id": 2, "temp": 66, "hour": 2},
        {"sensor_id": 2, "temp": 67, "hour": 3},
        {"sensor_id": 3, "temp": 80, "hour": 1},
        {"sensor_id": 3, "temp": 79, "hour": 2},
    ]

    result = find_consecutive_increases(readings)
    expected = [1, 2]
    print(f"Input: {len(readings)} readings")
    print(f"Output: {sorted(result)}")
    print(f"Expected: {sorted(expected)}")
    print("PASS" if sorted(result) == sorted(expected) else f"FAIL")
    print()

    print("Test 2: Find sensors with 2 consecutive increases")
    result2 = find_consecutive_increases(readings, consecutive_count=2)
    expected2 = [1, 2]
    print(f"Input: {len(readings)} readings, consecutive_count=2")
    print(f"Output: {sorted(result2)}")
    print(f"Expected: {sorted(expected2)}")
    print("PASS" if sorted(result2) == sorted(expected2) else f"FAIL")
