class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=list(s)
        d=-1
        for i in range(len(s)):
            b=s[i]
            a.pop(i)
            if b not in a:
                d=i
                return d
            a.insert(i,b)
        return d

