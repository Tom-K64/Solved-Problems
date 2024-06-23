"""
Problem Link:
https://leetcode.com/problems/solving-questions-with-brainpower/
"""

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            s = questions[i][1]
            if i + s + 1 < n:
                dp[i] += dp[i + s + 1]
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
