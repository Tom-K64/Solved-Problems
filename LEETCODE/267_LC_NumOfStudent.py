"""
Problem Link:
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""

class Solution:
  def countStudents(self, students, sandwiches):
    count = collections.Counter(students)

    for i, sandwich in enumerate(sandwiches):
      if count[sandwich] == 0:
        return len(sandwiches) - i
      count[sandwich] -= 1

    return 0
