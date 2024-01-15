"""
Problem Link:
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""

class Solution:
    def peakIndexInMountainArray(self, arr):
        index = 0
        while arr[index] < arr[index + 1]:
            index += 1
        return index
