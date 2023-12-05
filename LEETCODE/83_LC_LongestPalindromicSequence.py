"""
Problem Link:
https://leetcode.com/problems/longest-palindromic-subsequence/
"""

class Solution:
  def longestPalindromeSubseq(self, s):
    @functools.lru_cache(None)
    def dp(a, b):
      if a > b:
        return 0
      if a == b:
        return 1
      if s[a] == s[b]:
        return 2 + dp(a + 1, b - 1)
      return max(dp(a + 1, b), dp(a, b - 1))

    return dp(0, len(s) - 1)
