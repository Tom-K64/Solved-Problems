"""
Problem Link:
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
"""

class Solution:
  def findMaxK(self, nums):
    ans = -1
    seen = set()
    for num in nums:
      if -num in seen:
        ans = max(ans, abs(num))
      else:
        seen.add(num)
    return ans
