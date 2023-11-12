"""
Problem Link:
https://leetcode.com/problems/find-the-difference/
"""
class Solution:
  def findTheDifference(self, s, t):
    count = collections.Counter(s)
    for i, c in enumerate(t):
      count[c] -= 1
      if count[c] == -1:
        return c
