"""
Problem Link:
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
"""

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
        return (dfs(nums) - 1) % mod
