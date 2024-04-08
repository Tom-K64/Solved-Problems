"""
Problem Link:
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        answer = 0
        max_ = 0
        v = "aeiou"
        for i, c in enumerate(s):
            if c in v:
                max_ += 1
            if i >= k and s[i - k] in v:
                max_ -= 1
            answer = max(answer, max_)

        return answer
