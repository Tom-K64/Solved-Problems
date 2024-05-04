"""
Problem Link:
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""

class Solution:
  def maxDepth(self, s):
    ans = 0
    opened = 0
    for c in s:
      if c == '(':
        opened += 1
        ans = max(ans, opened)
      elif c == ')':
        opened -= 1

    return ans
