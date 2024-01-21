"""
Problem Link:
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, k):
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur) 
        add_parent(root, None)
        ans = []
        visited = set()
        def dfs(cur, distance):
            if not cur or cur in visited:
                return
            visited.add(cur)
            if distance == 0:
                ans.append(cur.val)
                return
            dfs(cur.parent, distance - 1)
            dfs(cur.left, distance - 1)
            dfs(cur.right, distance - 1)
        dfs(target, k)
        
        return ans
