"""
Problem Link:
https://leetcode.com/problems/number-of-flowers-in-full-bloom/
"""

class Solution:
  def fullBloomFlowers(self, flowers, persons):
    starts = sorted(s for s, _ in flowers)
    ends = sorted(e for _, e in flowers)
    return [bisect.bisect_right(starts, person) -
            bisect.bisect_left(ends, person)
            for person in persons]
