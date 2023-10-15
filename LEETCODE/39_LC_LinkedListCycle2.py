# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    s = head
    f = head
    while f and f.next:
      s = s.next
      f = f.next.next
      if s == f:
        s = head
        while s != f:
          s = s.next
          f = f.next
        return s
    return None

"""
Problem Link:
https://leetcode.com/problems/linked-list-cycle-ii/
"""
