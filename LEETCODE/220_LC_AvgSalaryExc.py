"""
Problem Link:
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)
