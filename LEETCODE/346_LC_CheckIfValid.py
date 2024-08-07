"""
Problem Link:
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
"""

class Solution:
    def validPartition(self, nums):
        n = len(nums)
        memo = {-1: True}
        def prefixIsValid(i):
            if i in memo:
                return memo[i]
            ans = False
            if i > 0 and nums[i] == nums[i - 1]:
                ans |= prefixIsValid(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= prefixIsValid(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= prefixIsValid(i - 3)
            memo[i] = ans
            return ans
        return prefixIsValid(n - 1)
