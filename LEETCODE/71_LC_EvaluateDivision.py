"""
Problem Link:
https://leetcode.com/problems/evaluate-division/
"""

class Solution:
  def calcEquation(self, equations, values, queries):
    answer = []
    graph = collections.defaultdict(dict)
    for (A, B), value in zip(equations, values):
      graph[A][B] = value
      graph[B][A] = 1 / value
    def devide(A, C, seen):
      if A == C:
        return 1.0
      seen.add(A)
      for B, value in graph[A].items():
        if B in seen:
          continue
        result = devide(B, C, seen)
        if result > 0:
          return value * result
      return -1.
    for A, C in queries:
      if A not in graph and C not in graph:
        answer.append(-1.0)
      else:
        answer.append(devide(A, C, set()))

    return answer
