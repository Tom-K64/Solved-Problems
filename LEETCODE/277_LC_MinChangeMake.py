"""
Problem Link:
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
"""

class Solution:
    def minOperations(self, s):
        start0 = 0
        start1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        return min(start0, start1)
