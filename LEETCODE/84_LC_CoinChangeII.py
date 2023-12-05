"""
Problem Link:
https://leetcode.com/problems/coin-change-ii/
"""

class Solution:
    def change(self, amount, coins):
        def numberOfWays(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]
            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)
            return memo[i][amount]
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return numberOfWays(0, amount)
