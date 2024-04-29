"""
Problem Link:
https://leetcode.com/problems/matrix-diagonal-sum/
"""

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n,s=len(mat)-1,0
        for i in range(n+1):
            if i!=(n-i):
                s+=mat[i][i]+mat[i][n-i]
            else:
                s+=mat[i][i]
        return s
