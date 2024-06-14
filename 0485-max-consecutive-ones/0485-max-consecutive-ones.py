class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if(sum(nums)==0):
            return 0
        if(len(nums)==1):
            return 1
        a=[]
        b=1
        h=len(nums)
        nums.append(0)
        for i in range(h):
            if(nums[i]==1):
                if(nums[i+1]==1):
                    b=b+1
                else:
                    a.append(b)
                    b=1
        return max(a)
        