"""
Problem Link:
https://leetcode.com/problems/validate-stack-sequences/
"""

class Solution:
  def validateStackSequences(self, pushed, popped):
    st = []
    i = 0
    for x in pushed:
      st.append(x)
      while st and st[-1] == popped[i]:
        st.pop()
        i += 1
    return not st
