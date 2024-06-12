"""
Problem Link:
https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
"""

class Solution:
  def eliminateMaximum(self, dist, speed):
    for i, arrivalTime in enumerate(sorted([(d - 1) // s for d, s in zip(dist, speed)])):
      if i > arrivalTime:
        return i
    return len(dist)
