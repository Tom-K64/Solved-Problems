class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols=("I","V","X","L","C","D","M")
        values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val=0
        for i in range(len(s)):
            if i==0:
                val=val+values[s[i]]
            else:
                val=val+values[s[i]]
                if symbols.index(s[i-1]) < symbols.index(s[i]):
                    val=val-(2*values[s[i-1]])
        return val


"""
Problem Link : https://leetcode.com/problems/roman-to-integer/
"""
