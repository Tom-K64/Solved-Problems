"""
Problem Link:
https://leetcode.com/problems/longest-cycle-in-a-graph/
"""

class Solution:
  def longestCycle(self, edges: List[int]) -> int:
    ans = -1
    t = 1
    tV = [0] * len(edges)
    for i, edge in enumerate(edges):
      if tV[i]:
        continue
      startTime = t
      u = i
      while u != -1 and not tV[u]:
        tV[u] = t
        t += 1
        u = edges[u]
      if u != -1 and tV[u] >= startTime:
        ans = max(ans, t - tV[u])

    return ans
