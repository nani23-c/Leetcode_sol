class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=[]
        k=0
        for i in range(len(nums)):
            if (i+1) not in nums:
                 k=i+1
        b=len(nums)*(len(nums)+1)/2
        b=sum(nums)+k-int(b)
        a.append(b)
        a.append(k)
        return a
