"""
Problem Link:
https://leetcode.com/problems/merge-strings-alternately/
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr=""
        l1,l2=len(word1),len(word2)
        length=int(max(l1,l2))
        for i in range(length):
            if i<l1:
                newstr+=word1[i]
            if i<l2:
                newstr+=word2[i]
        return newstr 
