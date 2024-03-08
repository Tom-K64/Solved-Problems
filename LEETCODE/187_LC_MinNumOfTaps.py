"""
Problem Link:
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
"""

class Solution:
    def minTaps(self, n, ranges):
        INF = int(1e9)
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            tap_start = max(0, i - ranges[i])
            tap_end = min(n, i + ranges[i])
            
            for j in range(tap_start, tap_end + 1):
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)
        if dp[n] == INF:
            return -1
        return dp[n]
