"""
Problem Link:
https://leetcode.com/problems/equal-row-and-column-pairs/
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count,n = 0,len(grid)
        for row in range(n):
            for col in range(n):
                match = True
                for i in range(n):
                    if grid[row][i] != grid[i][col]:
                        match = False
                        break
                count += int(match)
        return count
