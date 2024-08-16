"""
Problem Link:
https://leetcode.com/problems/total-cost-to-hire-k-workers/
"""

class Solution(object):
    def totalCost(self, costs, k, candidates):
        h_w = costs[:candidates]
        t_w = costs[max(candidates, len(costs) - candidates):]
        heapify(h_w)
        heapify(t_w)
        ans = 0
        n_h, n_t = candidates, len(costs) - 1 - candidates
        for _ in range(k): 
            if not t_w or h_w and h_w[0] <= t_w[0]: 
                ans += heappop(h_w)
                if n_h <= n_t: 
                    heappush(h_w, costs[n_h])
                    n_h += 1
            else: 
                ans += heappop(t_w)
                if n_h <= n_t:  
                    heappush(t_w, costs[n_t])
                    n_t -= 1
        return ans
