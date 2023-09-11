class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums:
                try:
                    return [i,nums.index(diff,i+1,)]
                except:
                    continue

"""
Problem Link :
https://leetcode.com/problems/two-sum/
"""
