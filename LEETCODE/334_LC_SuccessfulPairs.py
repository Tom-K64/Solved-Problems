"""
Problem Link:
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"""

class Solution:
  def successfulPairs(self, spells, potions, success):
    potions.sort()
    def firstIndexSuccess(spell):
      l = 0
      r = len(potions)
      while l < r:
        m = (l + r) // 2
        if spell * potions[m] >= success:
          r = m
        else:
          l = m + 1
      return l
    return [len(potions) - firstIndexSuccess(spell) for spell in spells]
