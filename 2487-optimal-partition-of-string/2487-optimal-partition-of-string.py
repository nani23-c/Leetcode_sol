class Solution:
    def partitionString(self, s: str) -> int:
        temp = ""
        ans,n = 0 ,len(s)
        for i in range(n-1):
            if s[i] in temp:
                ans+=1 
                temp = s[i]
            else:
                temp+=s[i]
        if s[-1] in temp:
            ans +=2 
        else:
            ans+=1 
        return ans


        