"""
Problem Link:
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""

class Solution:
  def pseudoPalindromicPaths(self, root):
    ans = 0

    def dfs(root, path):
      nonlocal ans
      if not root:
        return
      if not root.left and not root.right:
        path ^= 1 << root.val
        if path & (path - 1) == 0:
          ans += 1
        return

      dfs(root.left, path ^ 1 << root.val)
      dfs(root.right, path ^ 1 << root.val)

    dfs(root, 0)
    return ans
