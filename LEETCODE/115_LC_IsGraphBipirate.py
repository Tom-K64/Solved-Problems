"""
Problem Link:
https://leetcode.com/problems/is-graph-bipartite/
"""

from enum import Enum
class Color(Enum):
  kWhite = 0
  kRed = 1
  kGreen = 2

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = [Color.kWhite] * len(graph)
        for i in range(len(graph)):
            if colors[i] != Color.kWhite:
                continue
            colors[i] = Color.kRed
            q = collections.deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if colors[v] == colors[u]:
                        return False
                    if colors[v] == Color.kWhite:
                        colors[v] = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
                        q.append(v)
        return True
