"""
Problem Link:
https://leetcode.com/problems/build-an-array-with-stack-operations/
"""

class Solution:
  def buildArray(self, target, n):
    i,num,answer = 0,1,[]
    while i < len(target):
      t = target[i]
      if t == num:
        answer.append("Push")
        i += 1
      else:
        answer.append("Push")
        answer.append("Pop")
      num += 1
    return answer
