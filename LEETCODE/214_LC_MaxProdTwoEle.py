"""
Problem Link:
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1]
        y = nums[-2]
        return (x - 1) * (y - 1)
