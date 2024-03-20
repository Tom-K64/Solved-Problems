"""
Problem Link:
https://leetcode.com/problems/reducing-dishes/
"""

class Solution:
  def maxSatisfaction(self, satisfaction):
    temp = 0
    sS = 0
    for s in sorted(satisfaction, reverse=True):
      sS += s
      if sS <= 0:
        return temp
      temp += sS
    return temp
