class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                ans += (nums[i-1]+1-nums[i])
                nums[i]=nums[i-1]+1
        return ans        