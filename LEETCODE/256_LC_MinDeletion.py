"""
Problem Link:
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""

class Solution:
  def minDeletions(self, s):
    result = 0
    count = collections.Counter(s)
    usedFreq = set()
    for freq in count.values():
      while freq > 0 and freq in usedFreq:
        freq -= 1
        result += 1
      usedFreq.add(freq)

    return result
