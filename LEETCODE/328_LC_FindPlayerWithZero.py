"""
Problem Link:
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
"""

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [[] for _ in range(2)]
        lossesCount = collections.Counter()
        for winner, loser in matches:
            if winner not in lossesCount:
                lossesCount[winner] = 0
            lossesCount[loser] += 1
        for player, nLosses in lossesCount.items():
            if nLosses < 2:
                ans[nLosses].append(player)
        return [sorted(ans[0]), sorted(ans[1])]
