"""
Problem Link:
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""

class UnionFind:
  def __init__(self, n):
    self.id = list(range(n))
    self.rank = [0] * n

  def unionByRank(self, u, v):
    i = self.find(u)
    j = self.find(v)
    if i == j:
      return
    if self.rank[i] < self.rank[j]:
      self.id[i] = j
    elif self.rank[i] > self.rank[j]:
      self.id[j] = i
    else:
      self.id[i] = j
      self.rank[j] += 1

  def find(self, u):
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]

class Solution:
  def validPath(self, n, edges, source, destination):
    uf = UnionFind(n)

    for u, v in edges:
      uf.unionByRank(u, v)

    return uf.find(source) == uf.find(destination)
