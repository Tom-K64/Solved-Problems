"""
Problem Link:
https://leetcode.com/problems/find-the-pivot-integer/
"""

class Solution:
  def pivotInteger(self, n):
    y = (n * n + n) // 2
    x = int(math.sqrt(y))
    return x if x * x == y else -1
