class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n=amount
        mini = coins[0]
        dp=[0 for i in range(n+1)]
        for i in range(1,n+1):
            if i<mini:
                dp[i]=-1
            else:
                out=[]
                for j in coins:
                    if i >=j:
                        if dp[i-j] != -1:
                            out.append(dp[i-j])
                if len(out)==0:
                    dp[i]=-1
                else:
                    dp[i]=min(out)+1
        return dp[-1]
                