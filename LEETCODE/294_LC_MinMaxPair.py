"""
Problem Link:
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
"""

class Solution:
  def minPairSum(self, nums):
    nums.sort()
    res = max(nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2))
    return res
