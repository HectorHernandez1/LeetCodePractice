#!/bin/python3
"""
Data Engineering & Data Science Coding Practice Problems
=========================================================

These problems are common in data engineering/data science interviews.
They focus on data manipulation, aggregation, and analysis rather than
traditional algorithm problems.

Practice these with both pure Python and Pandas approaches where applicable.
"""

# ==============================================================================
# PROBLEM 1: Data Cleaning & Transformation (Easy-Medium)
# ==============================================================================

def clean_and_aggregate_sensors(sensor_data):
    """
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
    # TODO: Implement your solution here
    pass


def test_clean_and_aggregate_sensors():
    """Test cases for clean_and_aggregate_sensors"""
    sensor_data = [
        {"sensor_id": 1, "temperature": 72.5, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": None, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 1, "temperature": 75.0, "timestamp": "2026-01-15 11:00:00"},
        {"sensor_id": 3, "temperature": 68.2, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 2, "temperature": 70.0, "timestamp": "2026-01-15 11:00:00"},
    ]

    result = clean_and_aggregate_sensors(sensor_data)
    expected = {1: 73.75, 2: 70.0, 3: 68.2}

    print("Test 1:", "PASS" if result == expected else f"FAIL - Got {result}, Expected {expected}")

    # Edge case: all None values for a sensor
    edge_case = [
        {"sensor_id": 1, "temperature": None, "timestamp": "2026-01-15 10:00:00"},
        {"sensor_id": 1, "temperature": None, "timestamp": "2026-01-15 11:00:00"},
    ]
    result2 = clean_and_aggregate_sensors(edge_case)
    expected2 = {}
    print("Test 2 (Edge):", "PASS" if result2 == expected2 else f"FAIL - Got {result2}, Expected {expected2}")


# ==============================================================================
# PROBLEM 2: Grouping & Aggregation (Medium)
# ==============================================================================

def top_customers_by_spending(transactions, top_n=3):
    """
    Given a list of transactions, find the top N customers by total spending.

    Args:
        transactions: List of dicts with keys: customer_id, amount
        top_n: Number of top customers to return (default: 3)

    Returns:
        List of tuples [(customer_id, total_spending)] for top N customers,
        sorted by spending descending

    Example:
        Input:
        [
            {"customer_id": 1, "amount": 100},
            {"customer_id": 2, "amount": 150},
            {"customer_id": 1, "amount": 200},
            {"customer_id": 3, "amount": 50},
            {"customer_id": 2, "amount": 100},
            {"customer_id": 1, "amount": 50},
        ]

        Output:
        [(1, 350), (2, 250), (3, 50)]

    Time Complexity: O(n + k log k) where n is number of transactions, k is unique customers
    Space Complexity: O(k) where k is unique customers
    """
    # TODO: Implement your solution here
    pass


def test_top_customers_by_spending():
    """Test cases for top_customers_by_spending"""
    transactions = [
        {"customer_id": 1, "amount": 100},
        {"customer_id": 2, "amount": 150},
        {"customer_id": 1, "amount": 200},
        {"customer_id": 3, "amount": 50},
        {"customer_id": 2, "amount": 100},
        {"customer_id": 1, "amount": 50},
    ]

    result = top_customers_by_spending(transactions)
    expected = [(1, 350), (2, 250), (3, 50)]

    print("Test 1:", "PASS" if result == expected else f"FAIL - Got {result}, Expected {expected}")

    # Test with top_n = 2
    result2 = top_customers_by_spending(transactions, top_n=2)
    expected2 = [(1, 350), (2, 250)]
    print("Test 2:", "PASS" if result2 == expected2 else f"FAIL - Got {result2}, Expected {expected2}")


# ==============================================================================
# PROBLEM 3: Time Series Analysis (Medium)
# ==============================================================================

def find_consecutive_increases(readings, consecutive_count=3):
    """
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
    """
    # TODO: Implement your solution here
    # Hints:
    # 1. Group readings by sensor_id
    # 2. Sort each sensor's readings by hour
    # 3. For each sensor, check for consecutive increases
    # 4. Track consecutive increase count as you iterate
    pass


def test_find_consecutive_increases():
    """Test cases for find_consecutive_increases"""
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

    print("Test 1:", "PASS" if sorted(result) == sorted(expected) else f"FAIL - Got {result}, Expected {expected}")

    # Test with different consecutive_count
    result2 = find_consecutive_increases(readings, consecutive_count=2)
    expected2 = [1, 2]  # Both sensors have at least 2 consecutive increases
    print("Test 2:", "PASS" if sorted(result2) == sorted(expected2) else f"FAIL - Got {result2}, Expected {expected2}")


# ==============================================================================
# PROBLEM 4: Moving Average (Medium)
# ==============================================================================

def calculate_moving_average(values, window_size):
    """
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
    """
    # TODO: Implement your solution here
    # Hint: Use a sliding window approach for O(n) time complexity
    # Don't recalculate the sum for each window - subtract the left element and add the right element
    pass


def test_calculate_moving_average():
    """Test cases for calculate_moving_average"""
    values = [1, 2, 3, 4, 5, 6]
    window_size = 3

    result = calculate_moving_average(values, window_size)
    expected = [None, None, 2.0, 3.0, 4.0, 5.0]

    print("Test 1:", "PASS" if result == expected else f"FAIL - Got {result}, Expected {expected}")

    # Test with window_size = 1
    result2 = calculate_moving_average([1, 2, 3], 1)
    expected2 = [1.0, 2.0, 3.0]
    print("Test 2:", "PASS" if result2 == expected2 else f"FAIL - Got {result2}, Expected {expected2}")


# ==============================================================================
# PROBLEM 5: Data Deduplication (Medium)
# ==============================================================================

def deduplicate_records(records, key_fields):
    """
    Remove duplicate records based on specified key fields, keeping the most recent record.

    Args:
        records: List of dicts, each with a 'timestamp' field and other data fields
        key_fields: List of field names to use for identifying duplicates

    Returns:
        List of deduplicated records, keeping the record with the latest timestamp
        for each unique combination of key_fields

    Example:
        Input:
        records = [
            {"id": 1, "name": "Alice", "timestamp": "2026-01-15 10:00:00", "value": 100},
            {"id": 1, "name": "Alice", "timestamp": "2026-01-15 11:00:00", "value": 150},
            {"id": 2, "name": "Bob", "timestamp": "2026-01-15 10:00:00", "value": 200},
            {"id": 1, "name": "Alice", "timestamp": "2026-01-15 09:00:00", "value": 50},
        ]
        key_fields = ["id", "name"]

        Output:
        [
            {"id": 1, "name": "Alice", "timestamp": "2026-01-15 11:00:00", "value": 150},
            {"id": 2, "name": "Bob", "timestamp": "2026-01-15 10:00:00", "value": 200},
        ]

    Time Complexity: O(n log n) for sorting by timestamp
    Space Complexity: O(n) for storing deduplicated records
    """
    # TODO: Implement your solution here
    # Hints:
    # 1. Group records by the key_fields
    # 2. For each group, keep only the record with the latest timestamp
    # 3. Use a dictionary with tuple of key_field values as the key
    pass


def test_deduplicate_records():
    """Test cases for deduplicate_records"""
    records = [
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 10:00:00", "value": 100},
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 11:00:00", "value": 150},
        {"id": 2, "name": "Bob", "timestamp": "2026-01-15 10:00:00", "value": 200},
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 09:00:00", "value": 50},
    ]

    result = deduplicate_records(records, key_fields=["id", "name"])

    # Check that we have 2 records
    if len(result) != 2:
        print("Test 1: FAIL - Wrong number of records")
    else:
        # Check Alice's record (should be the 11:00 one with value 150)
        alice_record = next((r for r in result if r["id"] == 1), None)
        if alice_record and alice_record["value"] == 150:
            print("Test 1: PASS")
        else:
            print("Test 1: FAIL - Alice's record is not the latest one")


# ==============================================================================
# PROBLEM 6: Pivot Table Implementation (Medium-Hard)
# ==============================================================================

def create_pivot_table(data, index_col, column_col, value_col, aggfunc='sum'):
    """
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
    """
    # TODO: Implement your solution here
    # Hints:
    # 1. Create a nested dictionary structure
    # 2. For each record, group by index_col and column_col
    # 3. Apply the aggregation function
    # 4. Handle different aggfunc values ('sum', 'mean', 'count', 'min', 'max')
    pass


def test_create_pivot_table():
    """Test cases for create_pivot_table"""
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

    print("Test 1:", "PASS" if result == expected else f"FAIL - Got {result}, Expected {expected}")


# ==============================================================================
# PROBLEM 7: ETL - Extract, Transform, Load (Hard)
# ==============================================================================

def etl_pipeline(raw_data, transformations, output_format='dict'):
    """
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
    """
    # TODO: Implement your solution here
    # Hints:
    # 1. Start with raw_data
    # 2. Apply each transformation in order
    # 3. Handle errors gracefully (try/except for each transformation)
    # 4. Return the final transformed data
    pass


def test_etl_pipeline():
    """Test cases for etl_pipeline"""
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

    print("Test 1:", "PASS" if result == expected else f"FAIL - Got {result}, Expected {expected}")


# ==============================================================================
# Main Test Runner
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA ENGINEERING & DATA SCIENCE CODING PRACTICE")
    print("=" * 70)
    print()

    print("Problem 1: Data Cleaning & Transformation")
    print("-" * 70)
    test_clean_and_aggregate_sensors()
    print()

    print("Problem 2: Grouping & Aggregation")
    print("-" * 70)
    test_top_customers_by_spending()
    print()

    print("Problem 3: Time Series Analysis")
    print("-" * 70)
    test_find_consecutive_increases()
    print()

    print("Problem 4: Moving Average")
    print("-" * 70)
    test_calculate_moving_average()
    print()

    print("Problem 5: Data Deduplication")
    print("-" * 70)
    test_deduplicate_records()
    print()

    print("Problem 6: Pivot Table Implementation")
    print("-" * 70)
    test_create_pivot_table()
    print()

    print("Problem 7: ETL Pipeline")
    print("-" * 70)
    test_etl_pipeline()
    print()

    print("=" * 70)
    print("Practice complete! Implement the functions marked with 'TODO'")
    print("=" * 70)
