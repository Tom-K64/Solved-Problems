class Solution:
  def searchMatrix(self, matrix, target):
    if not matrix:
      return False
    m,n,left = len(matrix),len(matrix[0]),0
    right = m * n
    while left < right:
      mid = (left + right) // 2
      i = mid // n
      j = mid % n
      if matrix[i][j] == target:
        return True
      if matrix[i][j] < target:
        left = mid + 1
      else:
        right = mid
    return False
"""
Problem Link :
https://leetcode.com/problems/search-a-2d-matrix/
"""
