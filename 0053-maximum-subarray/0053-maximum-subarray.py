class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float("-inf")
        max_end = 0 
        for i in range(len(nums)):
            max_end += nums[i]
            if(max < max_end):
                max = max_end 
            if max_end < 0:
                max_end = 0
        return max

        

        