"""
Problem Link:
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
"""

class Solution:
  def minCost(self, colors, neededTime):
    ans = 0
    maxNeededTime = neededTime[0]
    for i in range(1, len(colors)):
      if colors[i] == colors[i - 1]:
        ans += min(maxNeededTime, neededTime[i])
        maxNeededTime = max(maxNeededTime, neededTime[i])
      else:
        maxNeededTime = neededTime[i]
    return ans
