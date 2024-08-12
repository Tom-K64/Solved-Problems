"""
Problem Link:
https://leetcode.com/problems/minimize-maximum-of-array/
"""

class Solution:
  def minimizeArrayValue(self, nums):
    ansswer = 0
    pre = 0

    for i, num in enumerate(nums):
      pre += num
      preAvg = math.ceil(pre / (i + 1))
      ansswer = max(ansswer, preAvg)

    return ansswer
