class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        word2 = list(word2)
        a = len(word1)
        b = len(word2)
        dp = [[0 for i in range(b+1)]for j in range(a+1)]
        for i in range(1,a+1):
            dp[i][0]=i 
        for j in range(1,b+1):
            dp[0][j]=j
        for i in range(1,a+1):
            for j in range(1,b+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[a][b]
