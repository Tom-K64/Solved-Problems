"""
Problem Link:
https://leetcode.com/problems/diagonal-traverse-ii/
"""

class Solution:
    def findDiagonalOrder(self, nums):
        queue,result = deque([(0, 0)]),[]        
        while queue:
            row, col = queue.popleft()
            result.append(nums[row][col])            
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))                
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))        
        return result
