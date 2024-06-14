class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        a,b,c = len(s1),len(s2),len(s3)
        n = min(a,b,c)
        i = 0 
        if s1[i]!=s2[i] or s2[i]!=s3[i]:
            return -1
        while(i<n):
            if s1[i]==s2[i] and s2[i]==s3[i]:
                i +=1 
            else:
                return (a+b+c-3*i)
        if i==n:
            return a+b+c-3*i