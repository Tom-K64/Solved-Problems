"""
Problem Link:
https://leetcode.com/problems/longest-ideal-subsequence/
"""

class Solution:
  def longestIdealString(self, s, k):
    dp = [0] * 26
    for c in s:
      i = ord(c) - ord('a')
      dp[i] = 1 + self._getMaxReachable(dp, i, k)
    return max(dp)
  def _getMaxReachable(self, dp, i, k):
    first = max(0, i - k)
    last = min(25, i + k)
    maxReachable = 0
    for j in range(first, last + 1):
      maxReachable = max(maxReachable, dp[j])
    return maxReachable
