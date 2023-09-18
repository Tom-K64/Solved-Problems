from queue import PriorityQueue
class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    dum = ListNode(0)
    cur = dum
    pq = PriorityQueue()
    for i, lst in enumerate(lists):
      if lst:
        pq.put((lst.val, i, lst))
    while not pq.empty():
      _, i, mN = pq.get()
      if mN.next:
        pq.put((mN.next.val, i, mN.next))
      cur.next = mN
      cur = cur.next
    return dum.next

"""
Problem Link:
https://leetcode.com/problems/merge-k-sorted-lists/
"""
