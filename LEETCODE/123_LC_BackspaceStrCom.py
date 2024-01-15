"""
Problem Link:
https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
  def backspaceCompare(self, s, t):
    def backspace(s):
      stack = []
      for c in s:
        if c != '#':
          stack.append(c)
        elif stack:
          stack.pop()
      return stack
    return backspace(s) == backspace(t)
