"""
Problem Link:
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
"""

class Solution:
  def findArray(self, pref):
    ans = [0] * len(pref)
    ans[0] = pref[0]
    for i in range(1, len(ans)):
      ans[i] = pref[i] ^ pref[i - 1]
    return ans
