class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]: 
                for line in matrix:
                    ans.append(line.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]: 
                for line in matrix[::-1]:
                    ans.append(line.pop(0))
        return ans

"""
Problem Link:
https://leetcode.com/problems/spiral-matrix/
"""
