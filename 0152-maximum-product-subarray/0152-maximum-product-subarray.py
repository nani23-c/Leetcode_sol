class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curM,curm = 1,1
        ans = nums[0]
        for i in range(n):
            a,b,c = nums[i],nums[i]*curM,nums[i]*curm
            curM = max(a,b,c)
            curm = min(a,b,c)
            ans = max(curM,ans)
        return ans
        