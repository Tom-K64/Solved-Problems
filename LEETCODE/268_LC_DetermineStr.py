"""
Problem Link:
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""

class Solution:
  def halvesAreAlike(self, s):
    kVowels = 'aeiouAEIOU'
    aVowelsCount = sum(c in kVowels for c in s[:len(s) // 2])
    bVowelsCount = sum(c in kVowels for c in s[len(s) // 2:])
    return aVowelsCount == bVowelsCount
