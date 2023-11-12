"""
Problem Link:
https://leetcode.com/problems/linked-list-random-node/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: ListNode):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        p = int(random.random() * len(self.range))
        return self.range[p]
