class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=list(ransomNote)
        b=list(magazine)
        c=[]
        for i in range(len(a)):
            if a[i] in b:
                b.pop(b.index(a[i]))
                c.append(a[i])
        if(c==a):
            return True
        else:
            return False
        