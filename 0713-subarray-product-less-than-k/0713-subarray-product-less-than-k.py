class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0 
        n = len(nums)
        ans,product,left = 0,1,0
        for right in range(n):
            product = product*nums[right]
            while(left<=right and product>=k):
                product = product//nums[left]
                left+=1 
            ans+=(right-left+1)
        return ans
        