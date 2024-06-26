"""
Problem Link:
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
"""

class Solution:
  def firstPalindrome(self, words):
    def isPalindrome(s):
      i = 0
      j = len(s) - 1
      while i < j:
        if s[i] != s[j]:
          return False
        i += 1
        j -= 1
      return True
    return next((word for word in words if isPalindrome(word)), '')
