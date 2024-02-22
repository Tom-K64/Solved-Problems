"""
Problem Link:
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
"""

class Solution:
    def longestSubsequence(self, arr, difference):
        sequence = {}
        ans = 1
        for ele in arr:
            prev_ele = sequence.get(ele - difference, 0)
            sequence[ele] = prev_ele + 1
            ans = max(ans, sequence[ele])
            
        return ans
