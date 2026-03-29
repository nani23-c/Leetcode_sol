class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a = list(s1)
        b = list(s2)
        if a==b:
            return True 
        a[0],a[2]=a[2],a[0]
        if a==b:
            return True 
        a[1],a[3]=a[3],a[1]
        if a==b:
            return True 
        a[0],a[2]=a[2],a[0]
        if a==b:
            return True 
        return False
        
        
        
        