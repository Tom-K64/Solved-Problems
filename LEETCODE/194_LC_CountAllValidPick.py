"""
Problem Link:
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""

class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer=1
        for i in range(1, n + 1):
            answer = answer * i * (i * 2 - 1) % 1000000007
        return answer
