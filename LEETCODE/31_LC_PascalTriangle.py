class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            ans.append([1] * (i + 1))
        for i in range(2, numRows):
            for j in range(1, len(ans[i]) - 1):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans

"""
Problem Link:
https://leetcode.com/problems/pascals-triangle/
"""
