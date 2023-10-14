class Solution:
  def singleNumber(self, nums):
    ones = 0
    twos = 0
    for num in nums:
      ones ^= num & ~twos
      twos ^= num & ~ones
    return ones
"""
Problem Link:
https://leetcode.com/problems/single-number-ii/
"""
