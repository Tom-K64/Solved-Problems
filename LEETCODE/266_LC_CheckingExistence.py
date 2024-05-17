"""
Problem Link:
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            else:
                self.parent[yset] = xset
            if self.rank[xset] == self.rank[yset]:
                self.rank[xset] += 1
            return True
        return False

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        dsu = DSU(n)
        for i, q in enumerate(queries):
            queries[i].append(i)

        queries.sort(key=lambda q: q[2])
        edgeList.sort(key=lambda e: e[2])

        i = 0
        res = [False] * len(queries)
        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1

            if dsu.find(q[0]) == dsu.find(q[1]):
                res[q[3]] = True

        return res
