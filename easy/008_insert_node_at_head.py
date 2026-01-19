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
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node 


# Test cases
if __name__ == '__main__':
    # Test case 1: Build list from sample input
    print("Test 1:")
    llist = SinglyLinkedList()
    values = [383, 484, 392, 975, 321]
    print(f"Inserting values at head: {values}")

    for val in values:
        llist.head = insertNodeAtHead(llist.head, val)

    print("Output: ", end='')
    print_singly_linked_list(llist.head, '\n')
    # Expected output:
    # 321
    # 975
    # 392
    # 484
    # 383
    print()

    # Test case 2: Empty list, insert single element
    print("Test 2:")
    llist2 = SinglyLinkedList()
    print("Inserting single value: 42")
    llist2.head = insertNodeAtHead(llist2.head, 42)
    print("Output: ", end='')
    print_singly_linked_list(llist2.head)
    # Expected output: 42
    print()

    # Test case 3: Insert multiple elements
    print("Test 3:")
    llist3 = SinglyLinkedList()
    values3 = [1, 2, 3]
    print(f"Inserting values at head: {values3}")

    for val in values3:
        llist3.head = insertNodeAtHead(llist3.head, val)

    print("Output: ", end='')
    print_singly_linked_list(llist3.head, ' -> ')
    # Expected output: 3 -> 2 -> 1
