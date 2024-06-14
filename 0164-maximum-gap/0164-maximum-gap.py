class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0 
        nums.sort()
        m = 0
        for i in range(1,n):
            m = max(nums[i]-nums[i-1],m)
        return m
            
        