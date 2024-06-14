class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        temp = nums[0]
        n = len(nums)
        h = 0
        for i in range(1,n):
            if nums[i] == temp:
                k +=1 
            else:
                temp = nums[i]
                k = 1 
            if k>2:
                nums[i]=10**4+1
                h +=1
        nums.sort()
        return n-h
