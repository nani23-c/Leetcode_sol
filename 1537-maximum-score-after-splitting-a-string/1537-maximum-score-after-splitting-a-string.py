class Solution:
    def maxScore(self, s: str) -> int:
        n = s.count('1')
        l,r = 0 ,n
        ans = 0 
        for i in range(len(s)-1):
            if s[i]=='0':
                l+=1
            if s[i]=='1':
                r-=1
            ans = max(ans,l+r)
        return ans
            
            
        