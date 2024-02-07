"""
Problem Link:
https://leetcode.com/problems/uncrossed-lines/
"""

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ln1 = len(nums1)
        ln2 = len(nums2)
        dp = [[0] * (ln2 + 1) for _ in range(ln1 + 1)]
        for i in range(1, ln1 + 1):
            for j in range(1, ln2 + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 \
                    if nums1[i - 1] == nums2[j - 1] \
                    else max(dp[i - 1][j], dp[i][j - 1])
        return dp[ln1][ln2]
