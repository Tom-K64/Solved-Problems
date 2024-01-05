"""
Problem Link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        len_price = len(prices)
        h, f = [0] * len_price, [0] * len_price
        h[0] = -prices[0]
        for i in range(1, len_price):
            h[i] = max(h[i - 1], f[i - 1] - prices[i])
            f[i] = max(f[i - 1], h[i - 1] + prices[i] - fee)
        return f[-1]
