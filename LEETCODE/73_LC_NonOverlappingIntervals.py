"""
Problem Link:
https://leetcode.com/problems/non-overlapping-intervals/
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])
        answer = 0
        k = -inf
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                answer += 1
        return answer
