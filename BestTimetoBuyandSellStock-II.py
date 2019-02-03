class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        #min_price = prices[0]
        max_profit = 0
        
        for i in range(0, (len(prices)-1)):
            y = prices[i+1]-prices[i]
            max_profit += max(0,y)
        print (max_profit)
        #print (min_price)

s = Solution()
s.maxProfit([7,1,5,3,6,4])

