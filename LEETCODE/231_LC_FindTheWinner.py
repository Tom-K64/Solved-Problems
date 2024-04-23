"""
Problem Link:
https://leetcode.com/problems/find-the-winner-of-an-array-game/
"""

class Solution:
  def getWinner(self, arr, k):
    ans = arr[0]
    wins = 0
    i = 1
    while i < len(arr) and wins < k:
      if arr[i] > ans:
        ans = arr[i]
        wins = 1
      else:
        wins += 1
      i += 1
    return ans
