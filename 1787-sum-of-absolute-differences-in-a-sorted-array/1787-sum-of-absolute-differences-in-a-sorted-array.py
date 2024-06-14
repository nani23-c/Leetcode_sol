class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l_sum = 0 
        l= 0 
        n = len(nums)
        r = n
        r_sum = sum(nums)
        out = []
        for i in range(n):
            out.append(l*nums[i]-l_sum+r_sum-r*nums[i])
            l_sum += nums[i]
            r_sum -= nums[i]
            l+=1 
            r-=1
        return out
        