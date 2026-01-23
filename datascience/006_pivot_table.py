#!/bin/python3
"""
Problem: Pivot Table Implementation
Difficulty: Medium-Hard
Date: TBD

Description:
Create a pivot table from a list of records.

This is similar to pandas.pivot_table() but implemented from scratch.

Args:
    data: List of dicts containing the data
    index_col: Column name to use as row index
    column_col: Column name to use as column headers
    value_col: Column name containing values to aggregate
    aggfunc: Aggregation function ('sum', 'mean', 'count', 'min', 'max')

Returns:
    Dict of dicts representing the pivot table
    Format: {index_value: {column_value: aggregated_value}}

Example:
    Input:
    data = [
        {'date': '2026-01-01', 'product': 'A', 'sales': 100},
        {'date': '2026-01-01', 'product': 'B', 'sales': 150},
        {'date': '2026-01-02', 'product': 'A', 'sales': 120},
        {'date': '2026-01-02', 'product': 'B', 'sales': 160},
    ]

    Output (with aggfunc='sum'):
    {
        '2026-01-01': {'A': 100, 'B': 150},
        '2026-01-02': {'A': 120, 'B': 160}
    }

Time Complexity: O(n) where n is number of records
Space Complexity: O(n) in worst case (all unique combinations)

Hints:
1. Create a nested dictionary structure
2. For each record, group by index_col and column_col
3. Apply the aggregation function
4. Handle different aggfunc values ('sum', 'mean', 'count', 'min', 'max')
"""


def create_pivot_table(data, index_col, column_col, value_col, aggfunc='sum'):
    """
    Create a pivot table from a list of records.

    Args:
        data: List of dicts containing the data
        index_col: Column name to use as row index
        column_col: Column name to use as column headers
        value_col: Column name containing values to aggregate
        aggfunc: Aggregation function ('sum', 'mean', 'count', 'min', 'max')

    Returns:
        Dict of dicts representing the pivot table
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: Pivot table with sum aggregation")
    data = [
        {'date': '2026-01-01', 'product': 'A', 'sales': 100},
        {'date': '2026-01-01', 'product': 'B', 'sales': 150},
        {'date': '2026-01-02', 'product': 'A', 'sales': 120},
        {'date': '2026-01-02', 'product': 'B', 'sales': 160},
    ]

    result = create_pivot_table(data, 'date', 'product', 'sales', aggfunc='sum')
    expected = {
        '2026-01-01': {'A': 100, 'B': 150},
        '2026-01-02': {'A': 120, 'B': 160}
    }

    print(f"Input: {len(data)} records")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("PASS" if result == expected else f"FAIL")
