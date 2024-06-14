class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        a=1
        nums.sort()
        k=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                k=k+1
                if(i==len(nums)-1):
                    if a < k:
                            a=k
            elif(nums[i]-nums[i-1]==0):
                   k=k+0
                   if(i==len(nums)-1):
                        if a < k:
                            a=k
                   
                

            else:
                if a < k:
                    a=k
                k=1
                
        return a