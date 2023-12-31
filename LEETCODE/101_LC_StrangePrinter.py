"""
Problem Link:
https://leetcode.com/problems/strange-printer/
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        string_length = len(s)
        pattern = [[string_length] * string_length for _ in range(string_length)]
        for length in range(1, string_length + 1):
            for left in range(string_length - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        pattern[left][right] = min(pattern[left][right], 1 + pattern[j][i] + pattern[i + 1][right])
                if j == -1:
                    pattern[left][right] = 0
        return pattern[0][string_length - 1] + 1
