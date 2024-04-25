"""
Problem Link:
https://leetcode.com/problems/make-the-string-great/
"""

class Solution:
  def makeGood(self, s):
    ans = []
    for c in s:
      if ans and self._is_bad_pair(ans[-1], c):
        ans.pop()
      else:
        ans.append(c)
    return ''.join(ans)
  def _is_bad_pair(self, a, b):
    return a != b and a.lower() == b.lower()
