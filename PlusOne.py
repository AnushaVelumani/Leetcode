class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        mystring = ""

        for digit in digits:
            mystring += str(digit)
        d =(int(mystring)+1)
        
        x = [int(n) for n in str(d)]

        print(x)
            
s=Solution()
s.plusOne([4,3,2,9])
