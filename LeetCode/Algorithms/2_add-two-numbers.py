"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ans = ListNode()
        l3 = ans
        while (l1 or l2):
            Sum = l1.val + l2.val + carry
            carry = Sum // 10
            l3.next = ListNode(Sum % 10)
            l3 = l3.next
            l2 = (l2.next if l2 is not None else None)
            l1 = (l1.next if l1 is not None else None)
            
        if carry > 0:
            l3.next = ListNode(carry)
            
        return ans.next
