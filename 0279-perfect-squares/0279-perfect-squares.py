class Solution:
    def numSquares(self, n: int) -> int:
        coins = []
        temp = 1
        square = 1
        while(square<n+1):
            coins.append(square)
            temp +=1 
            square = temp * temp 
        dp = [0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            min = dp[i-1]
            for j in coins:
                if i>=j:
                    if min>dp[i-j]:
                        min = dp[i-j]
            dp[i]=1+min
        return dp[-1]


        