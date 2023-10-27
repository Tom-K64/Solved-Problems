"""
Problem Link:
https://leetcode.com/problems/add-digits/
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            num=sum(list(map(int,[i for i in str(num)])))
        return num
