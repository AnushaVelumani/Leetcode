import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #print(int(math.sqrt(x)))

        output = x**(1/2)
        print (int(output))

s=Solution()
s.mySqrt(71)
