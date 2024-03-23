"""
Problem Link:
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        MaxVal=max(candies)
        result=[]
        for i in candies:
            if (i+extraCandies)>=MaxVal:
                result.append(True)
            else:
                result.append(False)
        return result
