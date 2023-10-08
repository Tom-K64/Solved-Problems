class Solution:
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findMid(head: ListNode) -> ListNode:
      p = None
      s = head
      f = head
      while f and f.next:
        p = s
        s = s.next
        f = f.next.next
      p.next = None
      return s
    if not head:
      return None
    if not head.next:
      return TreeNode(head.val)
    m = findMid(head)
    root = TreeNode(m.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(m.next)
    return root

"""
Problem Link:
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""
