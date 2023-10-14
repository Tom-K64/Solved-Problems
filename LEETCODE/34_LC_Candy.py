class Solution:
  def candy(self, ratings):
    n,answer = len(ratings),0
    l,r=[1] * n,[1] * n
    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        l[i] = l[i - 1] + 1
    for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
        r[i] = r[i + 1] + 1
    for a, b in zip(l, r):
      answer += max(a, b)
    return answer
"""
Problem Link:
https://leetcode.com/problems/candy/
"""
