"""
Problem Link:
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
"""

class Solution:
    def minimumReplacement(self, nums):
        answer = 0
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            answer += num_elements - 1
            nums[i] = nums[i] // num_elements
        return answer
