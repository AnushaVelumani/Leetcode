class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rem = 0
        num = x
        while (num>0):
            rem = (rem*10)+(num%10)
            num = num//10
        if (x == rem):
            return True
        else:
            return False
            
        
            
        
