"""
Problem Link:
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
"""

class Solution:
    def numSpecial(self, mat):
        m,n,answer = len(mat),len(mat[0]),0
        row_count,col_count = [0] * m,[0] * n
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        answer += 1
        return answer
