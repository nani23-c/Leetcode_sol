class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        takesfirst,takeslast = [0]*n,[0]*n 
        takesfirst[0],takeslast[0] = nums[0],0
        if n>1:
            takesfirst[1] = max(nums[0],nums[1])
            takeslast[1]= nums[1]
        if n>2:
            for i in range(2,n):
                if i!=n-1:
                    takesfirst[i]=max(takesfirst[i-2]+nums[i],takesfirst[i-1])
                else:
                    takesfirst[i]=takesfirst[i-1]
                takeslast[i] = max((takeslast[i-2]+nums[i]),takeslast[i-1])
        return max(takesfirst[-1],takeslast[-1])

        