"""
Problem Link:
https://leetcode.com/problems/maximum-subsequence-score/
"""

class Solution:
    def maxScore(self, nums1, nums2, k):
        pp = [(a, b) for a, b in zip(nums1, nums2)]
        pp.sort(key = lambda x: -x[1])
        topheap = [x[0] for x in pp[:k]]
        topsum = sum(topheap)
        heapq.heapify(topheap)
        answer = topsum * pp[k - 1][1]
        for i in range(k, len(nums1)):
            topsum -= heapq.heappop(topheap)
            topsum += pp[i][0]
            heapq.heappush(topheap, pp[i][0])
            answer = max(answer, topsum * pp[i][1])
        return answer
            
