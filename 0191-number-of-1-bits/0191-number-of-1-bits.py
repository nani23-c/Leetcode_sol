class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0 
        while(n>0):
            k+=n%2
            n = n//2
        return k


        