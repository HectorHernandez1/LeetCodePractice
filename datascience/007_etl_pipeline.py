#!/bin/python3
"""
Problem: ETL - Extract, Transform, Load
Difficulty: Hard
Date: TBD

Description:
Implement a simple ETL pipeline that applies a series of transformations to data.

This simulates a real data engineering task where you need to:
1. Extract data (provided as raw_data)
2. Transform it through multiple steps
3. Load it in the desired format

Args:
    raw_data: List of dicts containing raw data
    transformations: List of transformation functions to apply in order
                    Each function takes a list of dicts and returns a list of dicts
    output_format: 'dict' or 'list' - format of the output

Returns:
    Transformed data in the specified output_format

Example:
    raw_data = [
        {'name': 'alice', 'age': '25', 'salary': '50000'},
        {'name': 'bob', 'age': '30', 'salary': '60000'},
    ]

    transformations = [
        lambda data: [{**d, 'name': d['name'].upper()} for d in data],  # Uppercase names
        lambda data: [{**d, 'age': int(d['age'])} for d in data],       # Convert age to int
        lambda data: [{**d, 'salary': int(d['salary'])} for d in data], # Convert salary to int
    ]

    Output:
    [
        {'name': 'ALICE', 'age': 25, 'salary': 50000},
        {'name': 'BOB', 'age': 30, 'salary': 60000},
    ]

Hints:
1. Start with raw_data
2. Apply each transformation in order
3. Handle errors gracefully (try/except for each transformation)
4. Return the final transformed data
"""


def etl_pipeline(raw_data, transformations, output_format='dict'):
    """
    Apply a series of transformations to data in an ETL pipeline.

    Args:
        raw_data: List of dicts containing raw data
        transformations: List of transformation functions to apply in order
        output_format: 'dict' or 'list' - format of the output

    Returns:
        Transformed data in the specified output_format
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: ETL pipeline with multiple transformations")
    raw_data = [
        {'name': 'alice', 'age': '25', 'salary': '50000'},
        {'name': 'bob', 'age': '30', 'salary': '60000'},
    ]

    transformations = [
        lambda data: [{**d, 'name': d['name'].upper()} for d in data],
        lambda data: [{**d, 'age': int(d['age'])} for d in data],
        lambda data: [{**d, 'salary': int(d['salary'])} for d in data],
    ]

    result = etl_pipeline(raw_data, transformations)
    expected = [
        {'name': 'ALICE', 'age': 25, 'salary': 50000},
        {'name': 'BOB', 'age': 30, 'salary': 60000},
    ]

    print(f"Input: {len(raw_data)} records with {len(transformations)} transformations")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("PASS" if result == expected else f"FAIL")
