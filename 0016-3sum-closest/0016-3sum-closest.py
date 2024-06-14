class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        out = float("inf")
        n = len(nums)
        for i in range(n-2):
            j = i+1 
            k = n-1 
            while j < k:
                if abs(nums[i]+nums[j]+nums[k]-target)<= diff:
                    out = nums[i]+nums[j]+nums[k]
                    diff = abs(nums[i]+nums[j]+nums[k]-target)
                if nums[i]+nums[j]+nums[k]<target:
                    j +=1 
                elif nums[i]+nums[j]+nums[k]>target:
                    k = k-1 
                else:
                    return nums[i]+nums[j]+nums[k]
        return out




        