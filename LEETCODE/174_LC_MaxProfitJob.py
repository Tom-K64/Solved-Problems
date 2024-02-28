"""
Problem Link:
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""

class Solution:
  def jobScheduling(self, startTime, endTime, profit):
    dp = [0] * (len(startTime) + 1)
    jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
    for i in range(len(startTime)):
      startTime[i] = jobs[i][0]
    for i in reversed(range(len(startTime))):
      j = bisect.bisect_left(startTime, jobs[i][1])
      dp[i] = max(jobs[i][2] + dp[j], dp[i + 1])
    return dp[0]
