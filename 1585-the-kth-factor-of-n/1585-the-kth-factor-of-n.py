class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=1
        while(k>0):
            if(i>n):
                return -1
            if n%i==0:
                k=k-1
            if(k==0):
                return i
            i=i+1
            
        