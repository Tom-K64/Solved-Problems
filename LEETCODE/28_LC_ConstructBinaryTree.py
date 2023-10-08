# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, inorder, postorder):
    inToIndex = {num: i for i, num in enumerate(inorder)}

    def build(iS, iE, pS, pE):
      if iS > iE:
        return None
      rVal = postorder[pE]
      rIndex = inToIndex[rVal]
      lS = rIndex - iS

      r = TreeNode(rVal)
      r.left = build(iS, rIndex - 1,  pS, pS + lS - 1)
      r.right = build(rIndex + 1, iE,  pS + lS, pE - 1)
      return r
    return build(0, len(inorder) - 1, 0, len(postorder) - 1)

"""
Problem Link:
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
