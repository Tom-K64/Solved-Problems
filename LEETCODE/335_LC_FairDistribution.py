"""
Problem Link:
https://leetcode.com/problems/fair-distribution-of-cookies/
"""

class Solution:
    def distributeCookies(self, cookies, k):
        cur = [0] * k
        len_cookies = len(cookies)
        def dfs(i, count_zero):
            if len_cookies - i < count_zero:
                return float('inf')
            if i == len_cookies:
                return max(cur)
            ans = float('inf')
            for j in range(k):
                count_zero -= int(cur[j] == 0)
                cur[j] += cookies[i]
                ans = min(ans, dfs(i + 1, count_zero))
                cur[j] -= cookies[i]
                count_zero += int(cur[j] == 0)
            return ans
        return dfs(0, k)
