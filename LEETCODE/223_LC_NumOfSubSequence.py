"""
Problem Link:
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
"""

class Solution:
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        mod,ans = 10 ** 9 + 7,0
        nums.sort()
        for l in range(n):
            r = bisect.bisect_right(nums, target - nums[l]) - 1
            if r >= l:
                ans += pow(2, r - l, mod)
        return ans % mod
