"""
Problem Link:
https://leetcode.com/problems/boats-to-save-people/
"""

class Solution:
  def numRescueBoats(self, people, limit):
    answer,i,j = 0,0,len(people) - 1
    people.sort()
    while i <= j:
      rem = limit - people[j]
      j -= 1
      if people[i] <= rem:
        i += 1
      answer += 1
    return answer
