"""
Problem Link:
https://leetcode.com/problems/number-of-zero-filled-subarrays/
"""

class Solution(object):
  def zeroFilledSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    iBZ = -1
    for i, num in enumerate(nums):
      if num:
        iBZ = i
      else:
        a += i - iBZ
    return a
