class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i]<=min_price:
                min_price = prices[i]
            y = prices[i]-min_price
            if y>=max_profit:
                    max_profit = y
        print (max_profit)
        print (min_price)

s = Solution()
s.maxProfit([7,1,5,3,6,4])



