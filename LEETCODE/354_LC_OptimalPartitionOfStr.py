"""
Problem Link:
https://leetcode.com/problems/optimal-partition-of-string/
"""

class Solution:
  def partitionString(self, s: str) -> int:
    a = 1
    uM = 0
    for c in s:
      i = ord(c) - ord('a')
      if uM >> i & 1:
        uM = 1 << i
        a += 1
      else:
        uM |= 1 << i
    return a
