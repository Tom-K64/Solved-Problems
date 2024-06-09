"""
Problem Link:
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
"""

class Solution:
    def makeEqual(self, words):
        counts = [0] * 26
        for word in words:
            for c in word:
                counts[ord(c) - ord('a')] += 1
        n = len(words)
        for val in counts:
            if val % n != 0:
                return False
        return True
