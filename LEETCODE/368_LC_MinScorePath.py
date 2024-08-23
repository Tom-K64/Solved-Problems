"""
Problem Link:
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
"""

class Solution:
  def minScore(self, n, roads):
    a = math.inf
    gr = [[] for _ in range(n + 1)]
    q = collections.deque([1])
    seen = {1}
    for u, v, dis in roads:
      gr[u].append((v, dis))
      gr[v].append((u, dis))
    while q:
      u = q.popleft()
      for v, d in gr[u]:
        a = min(a, d)
        if v in seen:
          continue
        q.append(v)
        seen.add(v)
    return a
