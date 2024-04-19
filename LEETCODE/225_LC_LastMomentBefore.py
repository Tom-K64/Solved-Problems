"""
Problem Link:
https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""

class Solution:
    def getLastMoment(self, n, left, right):
        ans = 0
        for num in left:
            ans = max(ans, num)
        for num in right:
            ans = max(ans, n - num)
        return ans
