"""
Problem Link:
https://leetcode.com/problems/removing-stars-from-a-string/
"""

class Solution:
  def removeStars(self, s):
    answer = []
    for i in s:
      if i == '*':
        answer.pop()
      else:
        answer.append(i)
    return ''.join(answer)
