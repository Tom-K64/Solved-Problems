"""
Problem Link:
https://leetcode.com/problems/reconstruct-itinerary/
"""

class Solution:
  def findItinerary(self, tickets):
    ans = []
    graph = collections.defaultdict(list)
    for a, b in reversed(sorted(tickets)):
      graph[a].append(b)
    def dfs(u: str) -> None:
      while u in graph and graph[u]:
        dfs(graph[u].pop())
      ans.append(u)
    dfs('JFK')
    return ans[::-1]
