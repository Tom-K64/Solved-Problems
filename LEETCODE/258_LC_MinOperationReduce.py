"""
Problem Link:
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""

class Solution:
  def minOperations(self, nums, x):
    targetSum = sum(nums) - x
    if targetSum == 0:
      return len(nums)
    maxLen = self._maxSubArrayLen(nums, targetSum)
    return -1 if maxLen == -1 else len(nums) - maxLen
  def _maxSubArrayLen(self, nums, k):
    res = -1
    prefix = 0
    prefixToIndex = {0: -1}
    for i, num in enumerate(nums):
      prefix += num
      target = prefix - k
      if target in prefixToIndex:
        res = max(res, i - prefixToIndex[target])
      prefixToIndex[prefix] = i
    return res
