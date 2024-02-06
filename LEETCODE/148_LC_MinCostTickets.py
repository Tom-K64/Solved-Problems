"""
Problem Link:
https://leetcode.com/problems/minimum-cost-for-tickets/
"""

from functools import lru_cache
class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        D = [1, 7, 30]
        @lru_cache(None)
        def dp(i):
            if i >= n: return 0
            ans = float('inf')
            j = i
            for c, d in zip(costs, D):
                while j < n and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans
        return dp(0)
