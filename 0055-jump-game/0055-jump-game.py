class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visit = [False]*(n-1)
        visit +=[True]
        for i in range(n-2,-1,-1):
          for j in range(i,min(n,i+nums[i]+1)):
            if visit[j]:
              visit[i]=True 
              break 
        return visit[0]
          
