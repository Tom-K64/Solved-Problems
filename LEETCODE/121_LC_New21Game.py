"""
Problem Link:
https://leetcode.com/problems/new-21-game/
"""

class Solution:
  def new21Game(self, n, k, maxPts):
    if k == 0 or n >= k - 1 + maxPts:
      return 1.0
    ans = 0.0
    dp = [1.0] + [0] * n
    windowSum = dp[0]
    for i in range(1, n + 1):
      dp[i] = windowSum / maxPts
      if i < k:
        windowSum += dp[i]
      else:
        ans += dp[i]
      if i - maxPts >= 0:
        windowSum -= dp[i - maxPts]

    return ans
