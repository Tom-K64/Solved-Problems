"""
Problem Link:
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""

class Solution:
    def sortByBits(self, arr):
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr
