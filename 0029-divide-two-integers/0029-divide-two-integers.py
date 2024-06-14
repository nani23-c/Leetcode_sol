class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0 
        if (divisor * dividend)< 0:
            sign = -1
        else:
            sign = +1 
        upper_limit = 2**31-1
        lower_limit = -1*(2**31)
        ans = abs(dividend)//abs(divisor)
        ans = ans*sign
        if ans > upper_limit:
            return upper_limit
        elif ans < lower_limit:
            return lower_limit
        else:
            return ans

        