"""
Problem Link:
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""

class Solution:
  def maxCoins(self, piles):
    return sum(sorted(piles)[len(piles) // 3::2])
