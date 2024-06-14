class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    temp = target-(nums[i]+nums[j]+nums[k])
                    if temp in nums[k+1:]:
                        temp_list=[nums[i],nums[j],nums[k],temp]
                        if temp_list not in ans:
                            ans.append(temp_list)

        return ans
    
                