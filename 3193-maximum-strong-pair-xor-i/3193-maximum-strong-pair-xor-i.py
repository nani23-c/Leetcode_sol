class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0 
        for i in range(n):
            for j in range(i,n):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    x = nums[i] ^ nums[j]
                    if x>maxi:
                        maxi = x 
        return maxi