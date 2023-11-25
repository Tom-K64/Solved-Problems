"""
Problem Link:
https://leetcode.com/problems/poor-pigs/
"""

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        minutes = minutesToTest//minutesToDie
        res=0
        while ((minutes+1)**res)<buckets:
            res+=1
        return res
