"""
Problem Link:
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
"""

class Solution:
  def numRollsToTarget(self, n, k, target):
    dp = [1] + [0] * target
    for _ in range(n):
      newDp = [0] * (target + 1)
      for i in range(1, k + 1):
        for t in range(i, target + 1):
          newDp[t] += dp[t - i]
          newDp[t] %= 1000000007
      dp = newDp
    return dp[target]
