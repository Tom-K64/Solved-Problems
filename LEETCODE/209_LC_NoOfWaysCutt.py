"""
Problem Link:
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
"""

class Solution:
    def ways(self, pizza, k):
        rows = len(pizza)
        cols = len(pizza[0])
        app = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                app[row][col] = ((pizza[row][col] == 'A') + app[row + 1][col] + app[row][col + 1] - app[row + 1][col + 1])
        dpa = [[[0 for col in range(cols)] for row in range(rows)] for remain in range(k)]
        dpa[0] = [[int(app[row][col] > 0) for col in range(cols)]
             for row in range(rows)]
        mod = 1000000007
        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row + 1, rows):
                        if app[row][col] - app[next_row][col] > 0:
                            val += dpa[remain - 1][next_row][col]
                    for next_col in range(col + 1, cols):
                        if app[row][col] - app[row][next_col] > 0:
                            val += dpa[remain - 1][row][next_col]
                    dpa[remain][row][col] = val % mod
        return dpa[k - 1][0][0]
