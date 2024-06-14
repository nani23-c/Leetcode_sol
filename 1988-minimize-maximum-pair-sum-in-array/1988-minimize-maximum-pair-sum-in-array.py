class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxi = 0 
        for i in range(n//2):
            k = n-1-i
            h = nums[i]+nums[k]
            if h>maxi:
                maxi = h 
        return maxi

        