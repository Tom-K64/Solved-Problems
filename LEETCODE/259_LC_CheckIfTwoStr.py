"""
Problem Link:
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        final_word1 = "".join(word1)
        final_word2 = "".join(word2)
        if final_word1 == final_word2:
            return True
        else:
            return False
