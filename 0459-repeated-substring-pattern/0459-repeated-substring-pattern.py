class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n//2+1):
            if n%i == 0:
                rep = int(n/i)
                string = s[:i]
                og = string * rep 
                if og ==s:
                    return True 
        else:
            False

        
        