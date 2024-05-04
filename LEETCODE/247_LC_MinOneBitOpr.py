"""
Problem Link:
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
"""

class Solution:
  def minimumOneBitOperations(self, n):
    if n == 0:
      return 0
    x = 1 << n.bit_length() - 1
    return self.minimumOneBitOperations(n ^ (x | x >> 1)) + 1 + x - 1
