class Solution:
    def totalMoney(self, n: int) -> int:
        a=n%7
        b=n//7
        sum=b/2*(49+7*b)+b*a+(a*(a+1))/2
        sum=int(sum)
        return sum