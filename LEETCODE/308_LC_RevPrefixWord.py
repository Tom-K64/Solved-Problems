"""
Problem Link:
https://leetcode.com/problems/reverse-prefix-of-word/
"""

class Solution:
  def reversePrefix(self, word, ch):
    i = word.find(ch) + 1
    return word[:i][::-1] + word[i:]
