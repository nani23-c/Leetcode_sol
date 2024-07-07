class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while(numBottles>numExchange-1):
            left_out = numBottles%numExchange
            temp = numBottles//numExchange
            numBottles = temp+left_out 
            ans += temp
        return ans
        