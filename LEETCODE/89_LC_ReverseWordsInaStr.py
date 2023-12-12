"""
Problem Link:
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class Solution:
    def reverseWords(self, s):
        spaces=s.count(" ")
        if spaces:
            res=""
            words=s.split()
            for i in range(spaces):
                res+=words[i][::-1] + " "
            return res+words[spaces][::-1]
        else:
            return s[::-1]
