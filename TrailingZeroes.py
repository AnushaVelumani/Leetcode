class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        i = 5
        while i <= n:
            counter = counter + n//i
            i = i*5
            
        print (counter)

s = Solution()
s.trailingZeroes(1000)
