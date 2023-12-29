"""
Problem Link:
https://leetcode.com/problems/maximum-length-of-pair-chain/
"""

class Solution:
    def longestPairChain(self, i, pairs, n, memo):
        if memo[i] != 0:
            return memo[i]
        memo[i] = 1
        for ind in range(i + 1, n):
            if pairs[i][1] < pairs[ind][0]:
                memo[i] = max(memo[i], 1 + self.longestPairChain(ind, pairs, n, memo))
        return memo[i]
    def findLongestChain(self, pairs):
        len_pairs = len(pairs)
        pairs.sort()
        new_memo = [0] * len_pairs
        answer = 0
        for i in range(len_pairs):
            answer = max(answer, self.longestPairChain(i, pairs, len_pairs, new_memo))
        return answer
