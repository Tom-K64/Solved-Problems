"""
Problem Link:
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        cur,val = head,[]
        while cur:
            val.append(cur.val)
            cur = cur.next
        i ,j,maxSum= 0,len(val) - 1,0
        while(i < j):
            maxSum = max(maxSum, val[i] + val[j])
            i = i + 1
            j = j - 1
        return maxSum
