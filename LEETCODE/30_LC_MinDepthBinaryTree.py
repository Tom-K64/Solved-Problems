# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0        
        lft = self.minDepth(root.left)
        rht = self.minDepth(root.right)
        if root.left and root.right:
            return min(lft, rht) + 1
        return max(lft, rht) + 1

"""
Problem Link:
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
