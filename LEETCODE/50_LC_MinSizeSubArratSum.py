class Solution:
    def minSubArrayLen(self, target, nums):
        left,right,SOCW= 0,0,0
        res = float('inf')
        for right in range(0, len(nums)):
            SOCW += nums[right]
            while SOCW >= target:
                res = min(res, right - left + 1)
                SOCW -= nums[left]
                left += 1
        return res if res != float('inf') else 0
"""
Problem Link:
https://leetcode.com/problems/minimum-size-subarray-sum/
"""
