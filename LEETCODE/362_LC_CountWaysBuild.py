"""
Problem Link:
https://leetcode.com/problems/count-ways-to-build-good-strings/
"""

class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        answer,Mod,dp=0,(10**9)+7,[1] + [0] * high
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % Mod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % Mod
            if i >= low:
                answer = (answer + dp[i]) % Mod
        return answer
