class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            k=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    k=k+1
            a.append(k)
        return a
