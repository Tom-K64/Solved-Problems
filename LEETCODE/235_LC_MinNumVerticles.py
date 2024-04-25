"""
Problem Link:
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        all_nodes = set(range(n))
        dest_nodes = set(dest for _, dest in edges)
        src_nodes = all_nodes - dest_nodes
        return list(src_nodes)
