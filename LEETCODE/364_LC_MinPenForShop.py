"""
Problem Link:
https://leetcode.com/problems/minimum-penalty-for-a-shop/
"""

class Solution:
    def bestClosingTime(self, customers):
        cur_penalty = min_penalty = customers.count('Y')
        earliest_hour = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty
        return earliest_hour
