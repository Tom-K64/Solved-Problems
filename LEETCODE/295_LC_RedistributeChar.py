"""
Problem Link:
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
"""

class Solution:
  def reductionOperations(self, nums):
    result = 0
    nums.sort()
    for i in range(len(nums) - 1, 0, -1):
      if nums[i] != nums[i - 1]:
        result += len(nums) - i
    return result
