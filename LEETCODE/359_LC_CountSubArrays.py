"""
Problem Link:
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
"""

class Solution:
  def countSubarrays(self, nums, minK, maxK):
    ans = 0
    j = -1
    prevMinKIndex = -1
    prevMaxKIndex = -1

    for i, num in enumerate(nums):
      if num < minK or num > maxK:
        j = i
      if num == minK:
        prevMinKIndex = i
      if num == maxK:
        prevMaxKIndex = i
      ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

    return ans
