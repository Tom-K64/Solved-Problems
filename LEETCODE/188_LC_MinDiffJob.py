"""
Problem Link:
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
"""

class Solution:
  def minDifficulty(self, jobDifficulty, d):
    n = len(jobDifficulty)
    if d > n:
      return -1
    dp = [[math.inf] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
      for k in range(1, d + 1):
        maxDifficulty = 0
        for j in range(i - 1, k - 2, -1):
          maxDifficulty = max(maxDifficulty, jobDifficulty[j])
          dp[i][k] = min(dp[i][k], dp[j][k - 1] + maxDifficulty)

    return dp[n][d]
