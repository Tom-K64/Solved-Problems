"""
Problem Link:
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
"""

class Solution(object):
    def calc(self, s):
        return sum(int(c) for c in s)

    def numberOfBeams(self, bank):
        prc,result = 0,0
        for row in bank:
            crc = self.calc(row)
            if crc == 0:
                continue
            result += crc * prc
            prc = crc
        return result
