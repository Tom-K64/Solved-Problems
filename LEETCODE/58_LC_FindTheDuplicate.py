"""
Problem Link:
https://leetcode.com/problems/find-the-duplicate-number/
"""
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[nums[0]]
        f = nums[nums[nums[0]]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]
        s = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s
