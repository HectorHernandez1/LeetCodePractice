#!/bin/python3
"""
Problem: Linked List Cycle
Source: LeetCode #141
Difficulty: Easy
Date: 2026-02-10

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is used
to denote the index of the node that tail's next pointer is connected to. Note that
pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Function Description:
Complete the hasCycle function with the following parameters:
    head: Optional[ListNode] - head of the linked list

Returns:
    bool: True if there is a cycle, False otherwise

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow-up: Can you solve it using O(1) (i.e. constant) memory?

Examples:

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle using Floyd's algorithm.

        Args:
            head: Head of the linked list

        Returns:
            bool: True if cycle exists, False otherwise
        """
        # Write your code here
        if head is None or head.next is None:
            return False
        pt1 = head
        pt2 = head.next.next

        while pt2 is not None and pt2.next is not None:
            pt2 = pt2.next.next
            if pt1 == pt2:
                return True
            else:
                pt1 = pt1.next

                
        return False


# Helper functions for testing
def create_linked_list_with_cycle(arr, pos):
    """Create a linked list with a cycle at position pos."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i, val in enumerate(arr[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current

    # Create cycle
    if pos != -1:
        current.next = cycle_node

    return head


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1: Cycle exists
    print("Test 1:")
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    result = solution.hasCycle(head)
    print(f"Input: head = [3,2,0,-4], pos = 1")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 2: Cycle exists at head
    print("Test 2:")
    head = create_linked_list_with_cycle([1, 2], 0)
    result = solution.hasCycle(head)
    print(f"Input: head = [1,2], pos = 0")
    print(f"Output: {result}")
    print(f"Expected: True")
    print()

    # Test case 3: No cycle
    print("Test 3:")
    head = create_linked_list_with_cycle([1], -1)
    result = solution.hasCycle(head)
    print(f"Input: head = [1], pos = -1")
    print(f"Output: {result}")
    print(f"Expected: False")
    print()
