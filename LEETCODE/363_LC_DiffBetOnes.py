"""
Problem Link:
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
"""

class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])
        row_ones = [0] * m
        col_ones = [0] * n
        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n
        return grid
