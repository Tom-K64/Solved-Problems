"""
Problem Link:
https://leetcode.com/problems/furthest-building-you-can-reach/
"""

class Solution:
  def furthestBuilding(self, heights, bricks, ladders):
    minHeap = []

    for i, (a, b) in enumerate(itertools.pairwise(heights)):
      diff = b - a
      if diff <= 0:
        continue
      heapq.heappush(minHeap, diff)
      if len(minHeap) > ladders:
        bricks -= heapq.heappop(minHeap)
      if bricks < 0:
        return i

    return len(heights) - 1
