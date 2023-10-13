# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    answer = 0
    def dfstraverse(root: Optional[TreeNode], path: int) -> None:
      nonlocal answer
      if not root:
        return
      if not root.left and not root.right:
        answer += path * 10 + root.val
        return
      dfstraverse(root.left, path * 10 + root.val)
      dfstraverse(root.right, path * 10 + root.val)
    dfstraverse(root, 0)
    return answer
"""
Problem Link:
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""
