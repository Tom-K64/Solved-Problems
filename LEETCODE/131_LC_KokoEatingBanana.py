"""
Problem Link:
https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l = 1
    r = max(piles)
    def eatHours(m: int) -> int:
      return sum((pile - 1) // m + 1 for pile in piles)
    while l < r:
      m = (l + r) // 2
      if eatHours(m) <= h:
        r = m
      else:
        l = m + 1
    return l
