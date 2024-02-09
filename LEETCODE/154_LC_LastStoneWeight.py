"""
Problem Link:
https://leetcode.com/problems/last-stone-weight/
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            y=max(stones)
            stones.remove(y)
            x=max(stones)
            stones.remove(x)
            if x!=y:
                y=y-x
                stones.append(y)
            elif x==y:
                continue
        if len(stones)==0:
            return 0
        else:
            return stones[0]
