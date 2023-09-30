class Solution:
  def combine(self, n, k):
    ans = []
    def dfs(s, path):
      if len(path) == k:
        ans.append(path.copy())
        return
      for i in range(s, n + 1):
        path.append(i)
        dfs(i + 1, path)
        path.pop()
    dfs(1, [])
    return ans
"""
Problem Link :
https://leetcode.com/problems/simplify-path/
"""
