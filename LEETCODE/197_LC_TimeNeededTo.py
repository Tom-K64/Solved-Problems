"""
Problem Link:
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        a = [[] for _ in range(n)]
        answer = 0
        for i in range(n):
            if manager[i] != -1:
                a[manager[i]].append(i)
        q = deque([(headID, informTime[headID])])
        while q:
            size = len(q)
            for _ in range(size):
                t = q.popleft()
                for x in a[t[0]]:
                    if informTime[x] == 0:
                        answer = max(answer, t[1])
                    else:
                        q.append((x, t[1] + informTime[x]))
        return answer
