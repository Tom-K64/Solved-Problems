"""
Problem Link:
https://leetcode.com/problems/power-of-four/
"""

class Solution:
    def isPowerOfFour(self, n):
        if n > 0 and bin(n).count('1') == 1 and (n - 1) % 3 == 0:
            return True
        else:
            return False
