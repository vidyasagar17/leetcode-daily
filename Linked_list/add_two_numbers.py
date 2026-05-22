'''
2. Add Two Numbers
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/

Problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except 0 itself.

Example:
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807, returned in reverse order.

Approach:
Since digits are already in reverse order, we can add them like elementary
school addition (right to left). Walk both lists together, summing
corresponding digits plus any carry from the previous step.
For each step:
    total = val1 + val2 + carry
    new digit = total % 10
    carry    = total // 10
Use a dummy head node to simplify list construction.
Continue until both lists are exhausted AND carry is 0.

Time Complexity: O(max(m, n))   where m, n are the lengths of the two lists
Space Complexity: O(max(m, n))  for the result list
'''

from typing import Optional


# Definition for singly-linked list (provided by LeetCode).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
