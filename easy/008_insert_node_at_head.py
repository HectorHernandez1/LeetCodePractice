#!/bin/python3
"""
Problem: Insert a Node at the Head of a Linked List
Source: HackerRank (MyCodeSchool Tutorial Track)
Difficulty: Easy
Date: 2026-01-19

Description:
This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

Given a pointer to the head of a linked list, insert a new node before the head.
The next value in the new node should point to head and the data value should be
replaced with a given value. Return a reference to the new head of the list.
The head pointer given may be null meaning that the initial list is empty.

Function Description:
Complete the insertNodeAtHead function with the following parameters:
    llist: a reference to the head of a list
    data: the value to insert in the data field of the new node

Returns:
    SinglyLinkedListNode: reference to the new head of the list

Input Format:
The first line contains an integer n, the number of elements to be inserted at the head of the list.
The next n lines contain an integer each, the elements to be inserted, one per function call.

Constraints:
- 1 <= n <= 1000
- 1 <= data <= 1000

Sample Input:
5
383
484
392
975
321

Sample Output:
321
975
392
484
383

Explanation:
Initially the list is NULL. After inserting 383, the list is 383 -> NULL.
After inserting 484, the list is 484 -> 383 -> NULL.
After inserting 392, the list is 392 -> 484 -> 383 -> NULL.
After inserting 975, the list is 975 -> 392 -> 484 -> 383 -> NULL.
After inserting 321, the list is 321 -> 975 -> 392 -> 484 -> 383 -> NULL.
"""

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep=' '):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')
    print()


def insertNodeAtHead(llist, data):
    """
    Insert a new node at the head of a linked list.

    Args:
        llist: reference to the head of the linked list (may be None)
        data: the data value for the new node to insert

    Returns:
        SinglyLinkedListNode: reference to the new head of the linked list
    """
    # Write your code here
    pass 


# Test cases
if __name__ == '__main__':
    def to_list(node):
        """Convert a linked list to a Python list for easy assertions."""
        vals = []
        while node:
            vals.append(node.data)
            node = node.next
        return vals

    # Test case 1: Build list from sample input (head insert reverses order)
    llist = SinglyLinkedList()
    values = [383, 484, 392, 975, 321]
    for val in values:
        llist.head = insertNodeAtHead(llist.head, val)
    result = to_list(llist.head)
    print(f"Test 1: insert {values} at head -> {result}")
    assert result == [321, 975, 392, 484, 383], f"Got: {result}"

    # Test case 2: Empty list, insert single element
    llist2 = SinglyLinkedList()
    llist2.head = insertNodeAtHead(llist2.head, 42)
    result = to_list(llist2.head)
    print(f"Test 2: insert 42 into empty list -> {result}")
    assert result == [42], f"Got: {result}"

    # Test case 3: Insert multiple elements
    llist3 = SinglyLinkedList()
    values3 = [1, 2, 3]
    for val in values3:
        llist3.head = insertNodeAtHead(llist3.head, val)
    result = to_list(llist3.head)
    print(f"Test 3: insert {values3} at head -> {result}")
    assert result == [3, 2, 1], f"Got: {result}"

    print("All tests passed!")
