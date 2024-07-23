class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dict= {0:1}
        ans = 0
        nums = [0]+nums
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            if nums[i]-k in Dict:
                ans+=Dict[nums[i]-k ]
            if nums[i] in Dict:
                Dict[nums[i]]+=1 
            else:
                Dict[nums[i]]=1 
        return ans
        
        


        

        
        