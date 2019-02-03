class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """      
           
        if(x>0):
            rem =0
            while(x!=0):
                rem = (rem*10) +(x%10)
                x=x//10
                if rem > 2147483647:
                    return 0
            return(rem )
        else:
            val = (0 - int(str(0-x)[::-1]))
            if val < -2147483647:
                return 0
            return (val)
        
        
           
                
                    
