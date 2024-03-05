"""
Problem Link:
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""

class Solution:
  def minInsertions(self, s):
    """
    :type s: str
    :rtype: int
    """
    return len(s) - self._longestPalindromeSubseq(s)
  def _longestPalindromeSubseq(self, s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
      dp[i][i] = 1
    for d in range(1, n):
      for i in range(n - d):
        j = i + d
        if s[i] == s[j]:
          dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
