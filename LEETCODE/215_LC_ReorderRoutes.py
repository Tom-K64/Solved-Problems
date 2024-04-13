"""
Problem Link:
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""

class Solution:
    def dfs(self, al, visited, frnd):
        ch = 0
        visited[frnd] = True
        for tond in al[frnd]:
            if not visited[abs(tond)]:
                ch += self.dfs(al, visited, abs(tond)) + (1 if tond > 0 else 0)
        return ch

    def minReorder(self, n, connections):
        ai = [[] for _ in range(n)]
        for con in connections:
            ai[con[0]].append(con[1])
            ai[con[1]].append(-con[0])
        visited = [False] * n
        return self.dfs(ai, visited, 0)
