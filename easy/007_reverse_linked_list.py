#!/bin/python3
"""
Problem: Reverse a Linked List
Source: HackerRank / LeetCode #206
Difficulty: Easy
Date: 2026-01-16

Description:
Given the pointer to the head node of a linked list, change the next pointers of the nodes
so that their order is reversed. The head pointer given may be null meaning that the
initial list is empty.

Function Description:
Complete the reverse function with the following parameter:
    head: a reference to the head of a list

Returns:
    SinglyLinkedListNode: a reference to the head of the reversed list

Input Format:
The first line contains an integer n, the number of elements in the linked list.
The next n lines contain an integer each, the data values of the elements in the linked list.

Constraints:
- 1 <= n <= 1000
- 1 <= data <= 1000

Sample Input:
5
1
2
3
4
5

Sample Output:
5
4
3
2
1

Explanation:
The initial linked list is: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
After reversing, the linked list is: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
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

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


def print_singly_linked_list(node, sep=' '):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')
    print()


def reverse(head):
    """
    Reverse a linked list.

    Args:
        head: reference to the head of the linked list (may be None)

    Returns:
        SinglyLinkedListNode: reference to the head of the reversed linked list
    """
    # Write your code here
    
    pass

def reverseLoop(head):
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

    # Test case 1: Reverse list [1, 2, 3, 4, 5]
    llist = SinglyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        llist.insert_node(val)
    llist.head = reverse(llist.head)
    result = to_list(llist.head)
    print(f"Test 1: reverse [1, 2, 3, 4, 5] -> {result}")
    assert result == [5, 4, 3, 2, 1], f"Got: {result}"

    # Test case 2: Single element
    llist2 = SinglyLinkedList()
    llist2.insert_node(42)
    llist2.head = reverse(llist2.head)
    result = to_list(llist2.head)
    print(f"Test 2: reverse [42] -> {result}")
    assert result == [42], f"Got: {result}"

    # Test case 3: Two elements
    llist3 = SinglyLinkedList()
    llist3.insert_node(1)
    llist3.insert_node(2)
    llist3.head = reverse(llist3.head)
    result = to_list(llist3.head)
    print(f"Test 3: reverse [1, 2] -> {result}")
    assert result == [2, 1], f"Got: {result}"

    # Test case 4: Empty list
    llist4 = SinglyLinkedList()
    llist4.head = reverse(llist4.head)
    result = to_list(llist4.head)
    print(f"Test 4: reverse [] -> {result}")
    assert result == [], f"Got: {result}"

    print("All tests passed!")
