"""
Problem Link:
https://leetcode.com/problems/buddy-strings/
"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            frequency = [0] * 26
            for ch in s:
                frequency[ord(ch) - ord('a')] += 1
                if frequency[ord(ch) - ord('a')] == 2:
                    return True
            return False
        firstIndex = -1
        secondIndex = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIndex == -1:
                    firstIndex = i
                elif secondIndex == -1:
                    secondIndex = i
                else:
                    return False
        if secondIndex == -1:
            return False
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]
