"""
Problem Links:
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findMode(self, root):
    self.ans = []
    self.pred = None
    self.count = 0
    self.maxCount = 0
    def updateCount(root):
      if self.pred and self.pred.val == root.val:
        self.count += 1
      else:
        self.count = 1
      if self.count > self.maxCount:
        self.maxCount = self.count
        self.ans = [root.val]
      elif self.count == self.maxCount:
        self.ans.append(root.val)
      self.pred = root
    def inorder(root):
      if not root:
        return
      inorder(root.left)
      updateCount(root)
      inorder(root.right)
    inorder(root)
    return self.ans
