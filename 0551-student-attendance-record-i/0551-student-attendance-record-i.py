class Solution:
    def checkRecord(self, s: str) -> bool:
        a=1
        l=0
        for i in range(len(s)):
            if(s[i]=='A'):
                l=l+1
            if(i>1):
                if(s[i-2]=='L' and s[i-1]=='L' and s[i]=='L' ):
                   a=0
            
            
        if(l>1 or a==0):
            return False
        else:
            return True


        