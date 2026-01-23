#!/bin/python3
"""
Problem: Data Deduplication
Difficulty: Medium
Date: TBD

Description:
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

Hints:
1. Group records by the key_fields
2. For each group, keep only the record with the latest timestamp
3. Use a dictionary with tuple of key_field values as the key
"""


def deduplicate_records(records, key_fields):
    """
    Deduplicate records based on key fields, keeping the most recent.

    Args:
        records: List of dicts, each with a 'timestamp' field
        key_fields: List of field names to use for identifying duplicates

    Returns:
        List of deduplicated records
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == '__main__':
    print("Test 1: Deduplicate records by id and name")
    records = [
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 10:00:00", "value": 100},
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 11:00:00", "value": 150},
        {"id": 2, "name": "Bob", "timestamp": "2026-01-15 10:00:00", "value": 200},
        {"id": 1, "name": "Alice", "timestamp": "2026-01-15 09:00:00", "value": 50},
    ]

    result = deduplicate_records(records, key_fields=["id", "name"])

    print(f"Input: {len(records)} records")
    print(f"Output: {len(result)} unique records")

    # Check that we have 2 records
    if len(result) != 2:
        print("FAIL - Wrong number of records")
    else:
        # Check Alice's record (should be the 11:00 one with value 150)
        alice_record = next((r for r in result if r["id"] == 1), None)
        if alice_record and alice_record["value"] == 150:
            print(f"Alice's record: {alice_record}")
            print("PASS")
        else:
            print("FAIL - Alice's record is not the latest one")
