"""
Problem Link:
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum, ans, level = float('-inf'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_at_current_level += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level
        return ans
