class Solution:
  def convertToTitle(self, n: int) -> str:
    return self.convertToTitle((n - 1) // 26) + \
        chr(ord('A') + (n - 1) % 26) if n else ''/

"""
Problem Link:
https://leetcode.com/problems/excel-sheet-column-title/
"""
