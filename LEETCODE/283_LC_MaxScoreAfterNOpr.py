"""
Problem Link:
https://leetcode.com/problems/maximize-score-after-n-operations/
"""

class Solution:
    def backtrack(self, nums, mask, pairsPicked, memo):
        if 2 * pairsPicked == len(nums):
            return 0
        if memo[mask] != -1:
            return memo[mask]
        mS = 0
        for fI in range(len(nums)):
            for sI in range(fI + 1, len(nums)):
                if (mask >> fI) & 1 == 1 or (mask >> sI) & 1 == 1:
                    continue
                nM = mask | (1 << fI) | (1 << sI)
                cS = (pairsPicked + 1) * math.gcd(nums[fI], nums[sI])
                rS = self.backtrack(nums, nM, pairsPicked + 1, memo)
                mS = max(mS, cS + rS)
        memo[mask] = mS
        return mS
    
    def maxScore(self, nums):
        memoSize = 1 << len(nums)
        memo = [-1] * memoSize
        return self.backtrack(nums, 0, 0, memo)
