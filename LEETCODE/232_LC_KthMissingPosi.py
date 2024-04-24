"""
Problem Link:
https://leetcode.com/problems/kth-missing-positive-number/
"""

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        num=list(range(1,100000,1))
        for i in arr:
            num.remove(i)
        return num[k-1]
            
