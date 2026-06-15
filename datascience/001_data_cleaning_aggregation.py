#!/bin/python3
"""
Problem: Data Cleaning & Aggregation
Difficulty: Easy-Medium
Date: TBD

Description:
You have a list of dictionaries representing sensor readings.
Clean and transform the data.

Tasks:
1. Remove records with missing temperature values (None)
2. Calculate the average temperature for each sensor
3. Return a dictionary mapping sensor_id to average temperature

Args:
    sensor_data: List of dicts with keys: sensor_id, temperature, timestamp

Returns:
    Dict mapping sensor_id (int) to average temperature (float)

Example:
    Input:
    [
        {"sensor_id": 1, "temperature": 72.5, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": None, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 1, "temperature": 75.0, "timestamp": "2026-01-15 11:00:00"},
        {"sensor_id": 3, "temperature": 68.2, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": 70.0, "timestamp": "2026-01-15 11:00:00"},
    ]

    Output:
    {1: 73.75, 2: 70.0, 3: 68.2}
"""


def clean_and_aggregate_sensors(sensor_data):
    """
    Clean sensor data and calculate average temperature per sensor.

    Args:
        sensor_data: List of dicts with keys: sensor_id, temperature, timestamp

    Returns:
        Dict mapping sensor_id (int) to average temperature (float)
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: Basic sensor data")
    sensor_data = [
        {"sensor_id": 1, "temperature": 72.5, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": None, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 1, "temperature": 75.0, "timestamp": "2026-01-15 11:00:00"},
        {"sensor_id": 3, "temperature": 68.2, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": 70.0, "timestamp": "2026-01-15 11:00:00"},
    ]

    result = clean_and_aggregate_sensors(sensor_data)
    expected = {1: 73.75, 2: 70.0, 3: 68.2}
    print(f"Input: {len(sensor_data)} sensor readings")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("PASS" if result == expected else f"FAIL")
    print()

    print("Test 2: All None values for a sensor")
    edge_case = [
        {"sensor_id": 1, "temperature": None, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 1, "temperature": None, "timestamp": "2026-01-15 11:00:00"},
    ]
    result2 = clean_and_aggregate_sensors(edge_case)
    expected2 = {}
    print(f"Input: {len(edge_case)} sensor readings (all None)")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print("PASS" if result2 == expected2 else f"FAIL")
