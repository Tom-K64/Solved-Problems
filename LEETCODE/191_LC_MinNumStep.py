"""
Problem Link:
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
"""

class Solution:
  def minSteps(self, s, t):
    count = collections.Counter(s)
    count.subtract(collections.Counter(t))
    return sum(abs(value) for value in count.values())
