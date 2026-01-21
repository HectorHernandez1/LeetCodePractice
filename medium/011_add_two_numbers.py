#!/bin/python3
"""
Problem: Add Two Numbers
Source: LeetCode #2
Difficulty: Medium
Date: 2026-01-20

Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Function Description:
Complete the addTwoNumbers function with the following parameters:
    l1: ListNode - first linked list (digits in reverse order)
    l2: ListNode - second linked list (digits in reverse order)

Returns:
    ListNode: a linked list representing the sum (digits in reverse order)

Input Format:
Two linked lists representing non-negative integers in reverse order.

Constraints:
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros

Examples:

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists in reverse order.

        Args:
            l1: First linked list (digits in reverse)
            l2: Second linked list (digits in reverse)

        Returns:
            ListNode: Sum as a linked list (digits in reverse)
        """
        # Write your code here
        pass


# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Convert linked list to array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def print_linked_list(head, sep=' -> '):
    """Print linked list."""
    arr = linked_list_to_array(head)
    print(sep.join(map(str, arr)))


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1: 342 + 465 = 807
    print("Test 1:")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    print("l1: ", end='')
    print_linked_list(l1)
    print("l2: ", end='')
    print_linked_list(l2)
    result = solution.addTwoNumbers(l1, l2)
    print("Result: ", end='')
    print_linked_list(result)
    print(f"Expected: 7 -> 0 -> 8")
    print()

    # Test case 2: 0 + 0 = 0
    print("Test 2:")
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    print("l1: ", end='')
    print_linked_list(l1)
    print("l2: ", end='')
    print_linked_list(l2)
    result = solution.addTwoNumbers(l1, l2)
    print("Result: ", end='')
    print_linked_list(result)
    print(f"Expected: 0")
    print()

    # Test case 3: 9999999 + 9999 = 10009998
    print("Test 3:")
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    print("l1: ", end='')
    print_linked_list(l1)
    print("l2: ", end='')
    print_linked_list(l2)
    result = solution.addTwoNumbers(l1, l2)
    print("Result: ", end='')
    print_linked_list(result)
    print(f"Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1")
    print()

    # Test case 4: Different lengths - 99 + 1 = 100
    print("Test 4:")
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([1])
    print("l1: ", end='')
    print_linked_list(l1)
    print("l2: ", end='')
    print_linked_list(l2)
    result = solution.addTwoNumbers(l1, l2)
    print("Result: ", end='')
    print_linked_list(result)
    print(f"Expected: 0 -> 0 -> 1")
