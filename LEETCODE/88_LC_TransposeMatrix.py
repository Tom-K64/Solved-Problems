"""
Problem Link:
https://leetcode.com/problems/transpose-matrix/
"""
class Solution(object):
    def transpose(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
