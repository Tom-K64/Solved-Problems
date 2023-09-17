class Solution(object):
    def isValid(self, s):
        st = []
        for i in s:
            if i in '([{':
                st.append(i)
            else:
                if not st or \
                    (i == ')' and st[-1] != '(') or \
                    (i == '}' and st[-1] != '{') or \
                    (i == ']' and st[-1] != '['):
                    return False
                st.pop()
        return not st


"""
Problem Link :
https://leetcode.com/problems/valid-parentheses/
"""
