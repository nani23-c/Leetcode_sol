class Solution:
    def greatestLetter(self, s: str) -> str:
        a=[]
        max=0
        k=''

        for i in range(len(s)):
            if s[i].islower():
                if s[i].upper() in s:
                    a.append(s[i].upper())
            if s[i].isupper():
                if s[i].lower() in s:
                     a.append(s[i])
        if(len(a)>0):
            k=a[0]
            for i in range(len(a)):
               if(ord(k)<ord(a[i])):
                   k=a[i]
        return k


