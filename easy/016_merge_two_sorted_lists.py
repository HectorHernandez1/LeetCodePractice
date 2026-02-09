#!/bin/python3
"""
Problem: Merge Two Sorted Lists
Source: LeetCode #21
Difficulty: Easy
Date: TBD

Description:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Function Description:
Complete the mergeTwoLists function with the following parameters:
    list1: Optional[ListNode] - head of first sorted linked list
    list2: Optional[ListNode] - head of second sorted linked list

Returns:
    Optional[ListNode]: head of merged sorted linked list

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

Examples:

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.

        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list

        Returns:
            ListNode: Head of merged sorted linked list
        """
        # Write your code here
        #base case
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        
        # now merge
        pt1 = list1
        pt2 = list2
        head = ListNode()

        while pt1 is not None and pt2 is not None:
            if pt1.val < pt2.val:
                head.next = pt1
                head = head.next
                pt1 = pt1.next
            else:
                head.next = pt2
                head = head.next
                pt2 = pt2.next

        if pt1 is not None:
            head.next = pt1
        else:
            head.next = pt2
            
        return head.next

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


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    print("Test 1:")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Output: {linked_list_to_array(result)}")
    print(f"Expected: [1, 1, 2, 3, 4, 4]")
    print()

    # Test case 2
    print("Test 2:")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Input: list1 = [], list2 = []")
    print(f"Output: {linked_list_to_array(result)}")
    print(f"Expected: []")
    print()

    # Test case 3
    print("Test 3:")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Input: list1 = [], list2 = [0]")
    print(f"Output: {linked_list_to_array(result)}")
    print(f"Expected: [0]")
    print()
