"""
Problem Link:
https://leetcode.com/problems/smallest-number-in-infinite-set/
"""

class SmallestInfiniteSet(object):

    def __init__(self):
        self.is_present= set()
        self.added_integers= []
        self.current_integer = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.added_integers):
            answer = heapq.heappop(self.added_integers)
            self.is_present.remove(answer)
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.current_integer <= num or num in self.is_present:
            return
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
