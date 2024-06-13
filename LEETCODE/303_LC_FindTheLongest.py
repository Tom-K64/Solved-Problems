"""
Problem Link:
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
"""

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        ans,tail = [],[]
        for obstacle in obstacles:
            if not tail or obstacle >= tail[-1]:
                tail.append(obstacle)
                ans.append(len(tail))
            else:
                index = bisect_right(tail, obstacle)
                tail[index] = obstacle
                ans.append(index + 1)
        return ans
