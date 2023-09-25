class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        num,r,c,d = 1,0,0,0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        while num <= n * n:
            matrix[r][c] = num
            num += 1
            nR = r + dr[d]
            nC = c + dc[d]
            if nR < 0 or nR >= n or nC < 0 or nC >= n or matrix[nR][nC] != 0:
                d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
        return matrix

"""
Problem Link:
https://leetcode.com/problems/spiral-matrix-ii/
"""
