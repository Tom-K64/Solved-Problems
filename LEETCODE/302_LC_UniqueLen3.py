"""
Problem Link:
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
"""

class Solution:
  def countPalindromicSubsequence(self, s):
    ans,first,last = 0,[len(s)] * 26,[0] * 26
    for i, c in enumerate(s):
      index = ord(c) - ord('a')
      first[index] = min(first[index], i)
      last[index] = i
    for f, l in zip(first, last):
      if f < l:
        ans += len(set(s[f + 1:l]))
    return ans
