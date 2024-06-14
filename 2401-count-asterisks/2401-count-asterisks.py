class Solution:
    def countAsterisks(self, s: str) -> int:
        k=0
        m=0
        for i in range(len(s)):
            if(s[i]=='|'):
                k=k+1
            if(k%2==0):
                if(s[i]=='*'):
                    m=m+1
        return m