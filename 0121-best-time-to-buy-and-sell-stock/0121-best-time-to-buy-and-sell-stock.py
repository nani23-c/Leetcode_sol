class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buy = prices[0]
        profit = 0
        prices = prices[1:]
        for sell in prices:
            if buy > sell:
                buy = sell
            elif sell - buy > profit:
                profit = sell - buy
        
        
        return profit
        