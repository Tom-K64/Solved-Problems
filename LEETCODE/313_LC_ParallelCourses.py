"""
Problem Link:
https://leetcode.com/problems/parallel-courses-iii/
"""

class Solution:
  def minimumTime(self, n, relations, time):
    graph = [[] for _ in range(n)]
    inDegree = [0] * n
    dist = time.copy()
    for a, b in relations:
      u = a - 1
      v = b - 1
      graph[u].append(v)
      inDegree[v] += 1
    q = collections.deque([i for i, d in enumerate(inDegree) if d == 0])
    while q:
      u = q.popleft()
      for v in graph[u]:
        dist[v] = max(dist[v], dist[u] + time[v])
        inDegree[v] -= 1
        if inDegree[v] == 0:
          q.append(v)
    return max(dist)
