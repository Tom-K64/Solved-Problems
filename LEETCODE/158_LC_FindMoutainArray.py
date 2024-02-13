"""
Problem Link:
https://leetcode.com/problems/find-in-mountain-array/
"""

class Solution:
  def findInMountainArray(self, target, mountain_arr):
    n = mountain_arr.length()
    peakIndex = self.peakIndexInMountainArray(mountain_arr, 0, n - 1)

    leftIndex = self.searchLeft(mountain_arr, target, 0, peakIndex)
    if mountain_arr.get(leftIndex) == target:
      return leftIndex

    rightIndex = self.searchRight(mountain_arr, target, peakIndex + 1, n - 1)
    if mountain_arr.get(rightIndex) == target:
      return rightIndex

    return -1

  def peakIndexInMountainArray(self, A, l, r):
    while l < r:
      m = (l + r) // 2
      if A.get(m) < A.get(m + 1):
        l = m + 1
      else:
        r = m
    return l

  def searchLeft(self, A, target, l, r):
    while l < r:
      m = (l + r) // 2
      if A.get(m) < target:
        l = m + 1
      else:
        r = m
    return l

  def searchRight(self, A, target, l, r):
    while l < r:
      m = (l + r) // 2
      if A.get(m) > target:
        l = m + 1
      else:
        r = m
    return l
