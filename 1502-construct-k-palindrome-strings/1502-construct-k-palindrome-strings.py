class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dicti = {}
        n = len(s)
        if n<k:
            return False
        for i in range(n):
            if s[i] in dicti:
                dicti[s[i]]+=1
            else:
                dicti[s[i]]=1
        ans = 0 
        for i in dicti:
            if dicti[i]%2!=0:
                ans+=1
        if ans<=k:
            return True
        return False