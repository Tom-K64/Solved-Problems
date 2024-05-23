"""
Problem Link:
https://leetcode.com/problems/count-number-of-homogenous-substrings/
"""

class Solution:
  def countHomogenous(self, s):
    ans,count,currentChar = 0,0,'@'
    for c in s:
      count = count + 1 if c == currentChar else 1
      currentChar = c
      ans += count
      ans %= 1000000007
    return ans
