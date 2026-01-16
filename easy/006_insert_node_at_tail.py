#!/bin/python3
"""
Problem: Insert a Node at the Tail of a Linked List
Source: HackerRank (MyCodeSchool Tutorial Track)
Difficulty: Easy
Date: 2026-01-16

Description:
This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

You are given the pointer to the head node of a linked list and an integer to add to the list.
Create a new node with the given integer. Insert this node at the tail of the linked list
and return the head node of the linked list formed after inserting this new node.
The given head pointer may be null, meaning that the initial list is empty.

Function Description:
Complete the insertNodeAtTail function with the following parameters:
    head: a reference to the head of a list
    data: the data value for the node to insert

Returns:
    SinglyLinkedListNode: reference to the head of the modified linked list

Input Format:
The first line contains an integer n, the number of elements in the linked list.
The next n lines contain an integer each, the value that needs to be inserted at tail.

Constraints:
- 1 <= n <= 1000
- 1 <= data <= 1000

Sample Input:
5
141
302
164
530
474

Sample Output:
141
302
164
530
474

Explanation:
First the linked list is NULL. After inserting 141, the list is 141 -> NULL.
After inserting 302, the list is 141 -> 302 -> NULL.
After inserting 164, the list is 141 -> 302 -> 164 -> NULL.
After inserting 530, the list is 141 -> 302 -> 164 -> 530 -> NULL.
After inserting 474, the list is 141 -> 302 -> 164 -> 530 -> 474 -> NULL, which is the final list.
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


def insertNodeAtTail(head, data):
    """
    Insert a new node at the tail of a linked list.

    Args:
        head: reference to the head of the linked list (may be None)
        data: the data value for the new node to insert

    Returns:
        SinglyLinkedListNode: reference to the head of the modified linked list
    """
    # Write your code here
    pass


# Test cases
if __name__ == '__main__':
    # Test case 1: Build list from sample input
    print("Test 1:")
    llist = SinglyLinkedList()
    values = [141, 302, 164, 530, 474]
    print(f"Inserting values: {values}")

    for val in values:
        llist.head = insertNodeAtTail(llist.head, val)

    print("Output: ", end='')
    print_singly_linked_list(llist.head, '\n')
    # Expected output:
    # 141
    # 302
    # 164
    # 530
    # 474
    print()

    # Test case 2: Empty list, insert single element
    print("Test 2:")
    llist2 = SinglyLinkedList()
    print("Inserting single value: 42")
    llist2.head = insertNodeAtTail(llist2.head, 42)
    print("Output: ", end='')
    print_singly_linked_list(llist2.head)
    # Expected output: 42
    print()

    # Test case 3: Insert multiple elements
    print("Test 3:")
    llist3 = SinglyLinkedList()
    values3 = [1, 2, 3]
    print(f"Inserting values: {values3}")

    for val in values3:
        llist3.head = insertNodeAtTail(llist3.head, val)

    print("Output: ", end='')
    print_singly_linked_list(llist3.head, ' -> ')
    # Expected output: 1 -> 2 -> 3
