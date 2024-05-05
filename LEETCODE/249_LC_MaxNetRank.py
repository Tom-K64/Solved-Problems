"""
Problem Link:
https://leetcode.com/problems/maximal-network-rank/
"""

class Solution:
    def maximalNetworkRank(self, n, roads):
        maxR = 0
        adjacent = defaultdict(set)
        for road in roads:
            adjacent[road[0]].add(road[1])
            adjacent[road[1]].add(road[0])
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                curRank = len(adjacent[node1]) + len(adjacent[node2])
                if node2 in adjacent[node1]:
                    curRank -= 1
                maxR = max(maxR, curRank)
        return maxR
