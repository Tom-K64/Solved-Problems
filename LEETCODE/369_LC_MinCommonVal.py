"""
Problem Link:
https://leetcode.com/problems/minimum-common-value/
"""

class Solution:
  def getCommon(self, nums1, nums2):
    i,j=0,0
    while i < len(nums1) and j < len(nums2):
      if nums1[i] == nums2[j]:
        return nums1[i]
      if nums1[i] < nums2[j]:
        i += 1
      else:
        j += 1

    return -1
