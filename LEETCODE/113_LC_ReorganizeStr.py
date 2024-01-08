"""
Problem Link:
https://leetcode.com/problems/reorganize-string/
"""

class Solution:
    def reorganizeString(self, s):
        answer = []
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        while pq:
            count_first, char_first = heappop(pq)
            if not answer or char_first != answer[-1]:
                answer.append(char_first)
                if count_first + 1 != 0: 
                    heappush(pq, (count_first + 1, char_first))
            else:
                if not pq: return ''
                count_second, char_second = heappop(pq)
                answer.append(char_second)
                if count_second + 1 != 0:
                    heappush(pq, (count_second + 1, char_second))
                heappush(pq, (count_first, char_first))
        return ''.join(answer)
