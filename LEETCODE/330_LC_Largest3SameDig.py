"""
Problem Link:
https://leetcode.com/problems/largest-3-same-digit-number-in-string/
"""

class Solution:
    def largestGoodInteger(self, num):
        max_digit = '\0'
        for index in range(len(num) - 2):
            if num[index] == num[index + 1] == num[index + 2]:
                max_digit = max(max_digit, num[index])
        return '' if max_digit == '\0' else max_digit * 3
