"""
Problem Link:
https://leetcode.com/problems/longest-arithmetic-subsequence/
"""

class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dyn = {}
        for r in range(len(nums)):
            for l in range(0, r):
                dyn[(r, nums[r] - nums[l])] = dyn.get((l, nums[r] - nums[l]), 1) + 1  
        return max(dyn.values())
