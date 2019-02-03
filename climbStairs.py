class Solution:
    def climbStairs(self, n):
        a,b = 0,1
        for i in range(n):
            b,a=a+b,b
        return b
            

s = Solution()
print(s.climbStairs(3))
