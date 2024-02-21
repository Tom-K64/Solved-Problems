"""
Problem Link:
https://leetcode.com/problems/unique-number-of-occurrences/
"""

class Solution:
  def uniqueOccurrences(self, arr):
    count = collections.Counter(arr)
    occurrences = set()

    for value in count.values():
      if value in occurrences:
        return False
      occurrences.add(value)

    return True
