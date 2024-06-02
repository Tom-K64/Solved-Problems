"""
Problem Link:
https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""

class Solution:
  def maxFrequency(self, nums, k):
    ans,summ,temp = 0,0,0
    nums.sort()
    for index, num in enumerate(nums):
      summ += num
      while summ + k < num * (index - temp + 1):
        summ -= nums[temp]
        temp += 1
      ans = max(ans, index - temp + 1)
    return ans
