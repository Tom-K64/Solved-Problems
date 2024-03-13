"""
Problem Link:
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""

class Solution:
  def kWeakestRows(self, mat, k):
    candidates = []
    for i, row in enumerate(mat):
      candidates.append([sum(row), i])
    candidates.sort(key=lambda c: (c[0], c[1]))
    return [i for _, i in candidates[:k]]
