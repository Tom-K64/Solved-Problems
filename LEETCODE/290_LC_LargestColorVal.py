"""
Problem Link:
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
"""

class Solution:
  def largestPathValue(self, colors, edges):
    lenc = len(colors)
    ans = 0
    proc = 0
    graph = [[] for _ in range(lenc)]
    inDegree = [0] * lenc
    q = collections.deque()
    count = [[0] * 26 for _ in range(lenc)]
    for u, v in edges:
      graph[u].append(v)
      inDegree[v] += 1
    for i, degree in enumerate(inDegree):
      if degree == 0:
        q.append(i)
    while q:
      u = q.popleft()
      proc += 1
      count[u][ord(colors[u]) - ord('a')] += 1
      ans = max(ans, count[u][ord(colors[u]) - ord('a')])
      for v in graph[u]:
        for i in range(26):
          count[v][i] = max(count[v][i], count[u][i])
        inDegree[v] -= 1
        if inDegree[v] == 0:
          q.append(v)

    return ans if proc == lenc else -1
