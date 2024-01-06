"""
Problem Link:
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        temp,m=letters[0],min(letters)
        while m<=target:
            letters.remove(m)
            if len(letters)>0:
                m=min(letters)
            else:
                return temp
        return m
