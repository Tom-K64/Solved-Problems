"""
Problem Link:
https://leetcode.com/problems/split-linked-list-in-parts/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in xrange(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in xrange(k):
            head = cur
            for j in xrange(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
