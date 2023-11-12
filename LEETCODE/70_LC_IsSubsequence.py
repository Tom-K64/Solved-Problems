"""
Problem Link:
https://leetcode.com/problems/is-subsequence/
"""

class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subs=0
        for i in range(0,len(t)):
            if subs <= len(s) -1:
                print(s[subs])
                if s[subs]==t[i]:
                    subs+=1
        return  subs == len(s) 
