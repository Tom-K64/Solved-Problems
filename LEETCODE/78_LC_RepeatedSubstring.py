"""
Problem Link:
https://leetcode.com/problems/repeated-substring-pattern/
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False
