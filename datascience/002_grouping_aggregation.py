#!/bin/python3
"""
Problem: Grouping & Aggregation
Difficulty: Medium
Date: TBD

Description:
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


def top_customers_by_spending(transactions, top_n=3):
    """
    Find the top N customers by total spending.

    Args:
        transactions: List of dicts with keys: customer_id, amount
        top_n: Number of top customers to return (default: 3)

    Returns:
        List of tuples [(customer_id, total_spending)] for top N customers,
        sorted by spending descending
    """
    temp = {}
    for row in transactions:
        if row["customer_id"] not in temp:
            temp[row["customer_id"] ] = row["amount"] 
        else:
            temp[row["customer_id"]] += row["amount"] 
    # add as tuples
    final_list = []
    for k,v in temp.items():
        final_list.append((k,v))

    # sort
    return sorted(final_list, key=lambda x: x[1], reverse=True)[:top_n]



# Test cases
if __name__ == '__main__':
    print("Test 1: Top 3 customers")
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
    print(f"Input: {len(transactions)} transactions")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("PASS" if result == expected else f"FAIL")
    print()

    print("Test 2: Top 2 customers")
    result2 = top_customers_by_spending(transactions, top_n=2)
    expected2 = [(1, 350), (2, 250)]
    print(f"Input: {len(transactions)} transactions, top_n=2")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print("PASS" if result2 == expected2 else f"FAIL")
