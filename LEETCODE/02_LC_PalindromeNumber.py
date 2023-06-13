class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            temp=x
            newnum=0
            while temp>0:
                rem=temp%10
                temp=int(temp/10)
                newnum= (newnum*10)+rem
            if newnum==x:
                return True
            else:
                return False
      
"""
Problem Link :
https://leetcode.com/problems/palindrome-number/
"""
