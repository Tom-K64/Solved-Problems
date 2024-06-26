"""
Problem Link:
https://leetcode.com/problems/string-compression-ii/
"""

class Solution:
  def getLengthOfOptimalCompression(self, s, k):
    def getLength(maxFreq):
      if maxFreq == 1:
        return 1
      if maxFreq < 10:
        return 2
      if maxFreq < 100:
        return 3
      return 4

    @functools.lru_cache(None)
    def dp(i, k):
      if k < 0:
        return math.inf
      if i == len(s) or len(s) - i <= k:
        return 0
      ans = math.inf
      maxFreq = 0
      count = collections.Counter()
      for j in range(i, len(s)):
        count[s[j]] += 1
        maxFreq = max(maxFreq, count[s[j]])
        ans = min(ans, getLength(maxFreq) +
                  dp(j + 1, k - (j - i + 1 - maxFreq)))

      return ans

    return dp(0, k)
