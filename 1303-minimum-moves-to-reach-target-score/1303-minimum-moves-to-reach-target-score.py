class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0 
        while(maxDoubles>0):
            if target==1:
                return ans
            if target%2==0:
                ans+=1
                target=target//2 
                maxDoubles-=1
            else:
                ans+=1
                target-=1
        return ans+target-1

        