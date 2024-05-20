"""
Problem Link:
https://leetcode.com/problems/find-the-highest-altitude/
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        hp = cur_alt
        for altitude_gain in gain:
            cur_alt += altitude_gain
            hp = max(hp, cur_alt)
        return hp
