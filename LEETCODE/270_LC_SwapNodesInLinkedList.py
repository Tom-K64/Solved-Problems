"""
Problem Link:
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ln = head
        for i in range(1, k):
            ln = ln.next
        rn = head
        cur = ln
        while cur.next:
            cur = cur.next
            rn = rn.next
        ln.val, rn.val = rn.val, ln.val
        
        return head
