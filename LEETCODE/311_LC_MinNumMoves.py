"""
Problem Link:
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
"""

class Solution:
  def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))
