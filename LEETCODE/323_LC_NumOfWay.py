"""
Problem Link:
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
"""

class Solution:
  def numberOfWays(self, corridor):
    result,prevSeat,numSeats = 1,-1,0
    for i, c in enumerate(corridor):
      if c == 'S':
        numSeats += 1
        if numSeats > 2 and numSeats & 1:
          result = result * (i - prevSeat) % 1000000007
        prevSeat = i
    if numSeats > 1 and numSeats % 2 == 0:
        return result
    else:
        return 0
