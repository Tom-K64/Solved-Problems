"""
Problem Link:
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
"""

class Solution:
  def maxWidthOfVerticalArea(self, points):
    xs = sorted([x for x, _ in points])
    return max(b - a for a, b in itertools.pairwise(xs))
