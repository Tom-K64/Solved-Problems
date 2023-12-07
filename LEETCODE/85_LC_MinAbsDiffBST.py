"""
Problem Link:
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeValues = []
        def dfs(node):
            if node is None:
                return
            nodeValues.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        nodeValues.sort()
        minDiff = 1e9
        for i in range(1, len(nodeValues)):
            minDiff = min(minDiff, nodeValues[i] - nodeValues[i-1])
        return minDiff
