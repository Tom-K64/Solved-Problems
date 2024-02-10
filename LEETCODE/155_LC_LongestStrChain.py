"""
Problem Link:
https://leetcode.com/problems/longest-string-chain/
"""

class Solution:
  def longestStrChain(self, words):
    wordsSet = set(words)
    @functools.lru_cache(None)
    def dp(s):
      result = 1
      for i in range(len(s)):
        pred = s[:i] + s[i + 1:]
        if pred in wordsSet:
          result = max(result, dp(pred) + 1)
      return result
    return max(dp(word) for word in words)
