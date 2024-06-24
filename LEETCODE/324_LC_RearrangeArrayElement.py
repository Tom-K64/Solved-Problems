"""
Problem Link:
https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

class Solution:
  def rearrangeArray(self, nums):
    ans,pos,neg = [],[],[]
    for num in nums:
      (pos if num > 0 else neg).append(num)

    for p, n in zip(pos, neg):
      ans += [p, n]

    return ans
