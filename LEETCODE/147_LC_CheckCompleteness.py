"""
Problem Link:
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        hm = {}
        global mhs
        mhs = 0
        
        def isCom(node: Optional[TreeNode], h: int) -> bool:
            global mhs
            if not node:
                if mhs > h:
                    return False
					
                if h not in hm:
                    hm[h]=1
					
                return True
            
            if h in hm:
                return False
            
            mhs=max(mhs, h)
            
            l = isCom(node.left, h+1)
            r = isCom(node.right, h+1)
            
            return l and r
        
        
        return isCom(root, 0)
