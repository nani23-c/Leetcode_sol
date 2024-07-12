class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        maxi = 0 
        if x>y:
            add1 = x
            add2 = y
            c1 = "ab"
            c2 = "ba"
        else:
            add1 = y 
            add2 = x
            c1 = "ba"
            c2 = "ab"
        n = len(s)
        s = list(s)
        for i in range(n-2,-1,-1):
            try:
                if s[i]+s[i+1]==c1:
                    maxi+=add1
                    s.pop(i+1)
                    s.pop(i)
            except:
                a = 0
        n = len(s)
        for i in range(n-2,-1,-1):
            try:
                if s[i]+s[i+1]==c2:
                    maxi+=add2
                    s.pop(i+1)
                    s.pop(i)
            except:
                a = 0
        
        return maxi
         

        



