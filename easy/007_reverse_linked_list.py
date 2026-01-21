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
    
    if head is None  or head.next is None:
        return head

    # recursively reverse the rest
    new_head =  reverse(head.next)

    temp = head.next

    # make next node back to current
    temp.next = head
    # break the forward link 
    head.next = None

    return new_head

def reverseLoop(head):                                                                    
    prev = None                                                                           
    curr = head                                                                           
                                                                                    
    while curr is not None:  # Loop while we have nodes to process                        
        next = curr.next      # Save next node FIRST                                      
        curr.next = prev      # Reverse the pointer                                       
        prev = curr           # Move prev forward                                         
        curr = next           # Move curr forward                                         
                                                                                    
    return prev  # prev is now at the head of reversed list                               
                                                            





# Test cases
if __name__ == '__main__':
    # Test case 1: Reverse list [1, 2, 3, 4, 5]
    print("Test 1:")
    llist = SinglyLinkedList()
    values = [1, 2, 3, 4, 5]
    for val in values:
        llist.insert_node(val)

    print(f"Original list: ", end='')
    print_singly_linked_list(llist.head, ' -> ')

    llist.head = reverse(llist.head)

    print(f"Reversed list: ", end='')
    print_singly_linked_list(llist.head, ' -> ')
    # Expected output: 5 -> 4 -> 3 -> 2 -> 1
    print()

    # Test case 2: Single element
    print("Test 2:")
    llist2 = SinglyLinkedList()
    llist2.insert_node(42)

    print(f"Original list: ", end='')
    print_singly_linked_list(llist2.head)

    llist2.head = reverse(llist2.head)

    print(f"Reversed list: ", end='')
    print_singly_linked_list(llist2.head)
    # Expected output: 42
    print()

    # Test case 3: Two elements
    print("Test 3:")
    llist3 = SinglyLinkedList()
    llist3.insert_node(1)
    llist3.insert_node(2)

    print(f"Original list: ", end='')
    print_singly_linked_list(llist3.head, ' -> ')

    llist3.head = reverse(llist3.head)

    print(f"Reversed list: ", end='')
    print_singly_linked_list(llist3.head, ' -> ')
    # Expected output: 2 -> 1
    print()

    # Test case 4: Empty list
    print("Test 4:")
    llist4 = SinglyLinkedList()

    print(f"Original list: (empty)")

    llist4.head = reverse(llist4.head)

    print(f"Reversed list: ", end='')
    if llist4.head is None:
        print("(empty)")
    else:
        print_singly_linked_list(llist4.head)
    # Expected output: (empty)
