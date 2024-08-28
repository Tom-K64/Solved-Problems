"""
Problem Link:
https://leetcode.com/problems/count-total-number-of-colored-cells/
"""

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=1
        for i in range (1,n):
            count=count+(4*i)
        return count
        
