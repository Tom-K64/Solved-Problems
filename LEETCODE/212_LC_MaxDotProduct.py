"""
Problem Link:
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
"""

class Solution:
  def maxDotProduct(self, A, B):
    m = len(A)
    n = len(B)
    dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j],max(0, dp[i][j]) + A[i] * B[j])
    return dp[m][n]
