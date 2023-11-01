"""
Problem Link:
https://leetcode.com/problems/remove-duplicate-letters/
"""

class Solution:
  def removeDuplicateLetters(self, s):
    ans = []
    count = collections.Counter(s)
    used = [False] * 26
    for c in s:
      count[c] -= 1
      if used[ord(c) - ord('a')]:
        continue
      while ans and ans[-1] > c and count[ans[-1]] > 0:
        used[ord(ans[-1]) - ord('a')] = False
        ans.pop()
      ans.append(c)
      used[ord(ans[-1]) - ord('a')] = True
    return ''.join(ans)
