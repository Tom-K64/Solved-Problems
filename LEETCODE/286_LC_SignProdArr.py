"""
Problem Link:
https://leetcode.com/problems/sign-of-the-product-of-an-array/
"""

from functools import reduce
class Solution(object):
    def signFunc(self,x):
        if x>1:
            return 1
        elif x<0:
            return -1
        else:
            return 0
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=reduce(lambda x,y:x*y,nums)
        return self.signFunc(x)
