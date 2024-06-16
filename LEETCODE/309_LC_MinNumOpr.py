"""
Problem Link:
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
"""

class Solution:
  def minOperations(self, nums):
    n = len(nums)
    ans = n
    nums = sorted(set(nums))
    for i, start in enumerate(nums):
      end = start + n - 1
      index = bisect_right(nums, end)
      uniqueLength = index - i
      ans = min(ans, n - uniqueLength)
    return ans
