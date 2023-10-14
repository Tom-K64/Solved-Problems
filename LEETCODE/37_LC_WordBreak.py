class Solution:
  def wordBreak(self, s, wordDict):
    n = len(s)
    maxLength = len(max(wordDict, key=len))
    wordSet = set(wordDict)
    dp = [True] + [False] * n
    for i in range(1, n + 1):
      for j in reversed(range(i)):
        if i - j > maxLength:
          break
        if dp[j] and s[j:i] in wordSet:
          dp[i] = True
          break
    return dp[n]
"""
Problem Link:
https://leetcode.com/problems/word-break/
"""
