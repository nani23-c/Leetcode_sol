class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        out = 0 
        for i in range(limit+1):
            for j in range(limit+1):
                k = n-i-j
                if k<limit+1 and k>=0:
                    out +=1
        return out

        