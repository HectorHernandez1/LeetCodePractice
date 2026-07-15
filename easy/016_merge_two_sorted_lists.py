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


# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = linked_list_to_array(solution.mergeTwoLists(list1, list2))
    print(f"Test 1: [1,2,4] + [1,3,4] -> {result} (expected [1, 1, 2, 3, 4, 4])")
    assert result == [1, 1, 2, 3, 4, 4], f"Got: {result}"

    # Test case 2: both empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = linked_list_to_array(solution.mergeTwoLists(list1, list2))
    print(f"Test 2: [] + [] -> {result} (expected [])")
    assert result == [], f"Got: {result}"

    # Test case 3: one empty
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = linked_list_to_array(solution.mergeTwoLists(list1, list2))
    print(f"Test 3: [] + [0] -> {result} (expected [0])")
    assert result == [0], f"Got: {result}"

    print("All tests passed!")
