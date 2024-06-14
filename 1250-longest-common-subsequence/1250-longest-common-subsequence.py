class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a,b =len(text1),len(text2)
        dp = [[0 for i in range(b+1)] for j in range(a+1)]
        for i in range(1,a+1):
            for j in range(1,b+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[a][b]