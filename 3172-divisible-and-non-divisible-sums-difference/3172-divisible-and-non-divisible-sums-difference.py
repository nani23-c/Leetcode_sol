class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0 
        for i in range(1,n+1):
            if i%m==0:
                sum1+=i 
        total = (((n)*(n+1))//2)-2*sum1
        return total