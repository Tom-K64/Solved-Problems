"""
Problem Link:
https://leetcode.com/problems/number-of-music-playlists/
"""

class Solution:
    def numMusicPlaylists(self, n, goal, k):
        MOD = 10**9 + 7
        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
        return dp[goal][n]
