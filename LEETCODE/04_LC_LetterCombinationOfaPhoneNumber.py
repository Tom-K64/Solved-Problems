class Solution:
  def letterCombinations(self, digits):
    if not digits:
      return []
    digitToLetters = ['', '', 'abc', 'def', 'ghi','jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []
    def dfs(i: int, path):
      if i == len(digits):
        ans.append(''.join(path))
        return
      for letter in digitToLetters[ord(digits[i]) - ord('0')]:
        path.append(letter)
        dfs(i + 1, path)
        path.pop()
    dfs(0, [])
    return ans

"""
Problem Link :
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
