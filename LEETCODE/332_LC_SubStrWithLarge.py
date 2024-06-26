"""
Problem Link:
https://leetcode.com/problems/substring-with-largest-variance/
"""

class Solution:
    def largestVariance(self, s):
        count1,count2,max_variance = 0,0,0
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]
        for runs in range(2):
            for pair in pairs:
                count1 = count2 = 0
                for letter in s:
                    if letter not in pair:
                        continue
                    if letter == pair[0]:
                        count1 += 1
                    elif letter == pair[1]:
                        count2 += 1
                    if count1 < count2:
                        count1 = count2 = 0
                    elif count1 > 0 and count2 > 0:
                        max_variance = max(max_variance, count1 - count2)
            s = s[::-1]
                
        return max_variance
