"""
Problem Link:
https://leetcode.com/problems/similar-string-groups/
"""

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        UF = {}
        ranks = defaultdict(int)
        def find(x):
            if x not in UF:
                UF[x] = x
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if ranks[rootX] < ranks[rootY]:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
                if ranks[rootX] == ranks[rootY]:
                    ranks[rootX] += 1
        def areNeighbors(a,b):
            dif = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    dif += 1
            return dif==0 or dif==2
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if areNeighbors(strs[i],strs[j]):
                    union(strs[i],strs[j])
        return len(set([find(x) for x in strs]))
