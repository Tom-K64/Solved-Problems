"""
Problem Link:
https://leetcode.com/problems/combination-sum-iv/
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [-1] * target
        def dfs(target):
            if target < 0:
                return 0
            if dp[target] != -1:
                return dp[target]
            dp[target] = sum(dfs(target - num) for num in nums)
            return dp[target]
        return dfs(target)
