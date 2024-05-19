"""
Problem Link:
https://leetcode.com/problems/largest-submatrix-with-rearrangements/
"""

class Solution:
  def largestSubmatrix(self, matrix):
    hist,result = [0] * len(matrix[0]),0
    for row in matrix:
      for i, num in enumerate(row):
        hist[i] = 0 if num == 0 else hist[i] + 1
      sortedHist = sorted(hist)
      for i, h in enumerate(sortedHist):
        result = max(result, h * (len(row) - i))
    return result
