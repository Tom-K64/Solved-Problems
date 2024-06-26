"""
Problem Link:
https://leetcode.com/problems/merge-in-between-linked-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeInBetween(self, list1, a, b, list2):
    nodeBeforeA = list1
    for i in range(a - 1):
      nodeBeforeA = nodeBeforeA.next

    nodeB = nodeBeforeA.next
    for i in range(b - a):
      nodeB = nodeB.next

    nodeBeforeA.next = list2
    lastNodeInList2 = list2

    while lastNodeInList2.next:
      lastNodeInList2 = lastNodeInList2.next

    lastNodeInList2.next = nodeB.next
    nodeB.next = None
    return list1
