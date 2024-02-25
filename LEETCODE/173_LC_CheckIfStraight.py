"""
Problem Link:
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
"""

class Solution:
  def checkStraightLine(self, coordinates):
    x0, y0, x1, y1 = *coordinates[0], *coordinates[1]
    dx = x1 - x0
    dy = y1 - y0

    return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates)
