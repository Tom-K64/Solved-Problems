"""
Problem Link:
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""

class Solution:
    def maxScore(self, s):
        ones,zeros,ans = s.count("1"),0,0
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans
