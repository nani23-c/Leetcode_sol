class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        Dict = {}
        Dict[0]=1
        ans = 0
        if nums[0]%2 !=0:
            nums[0]=1
            Dict[1]=1
            if nums[0]==k:
                ans+=1
        else:
            nums[0]=0 
            Dict[0]+=1
        for i in range(1,len(nums)):
            if nums[i]%2==1:
                nums[i]= nums[i-1]+1
            else:
                nums[i]= nums[i-1]
            if nums[i]-k in Dict:
                ans += Dict[nums[i]-k]
                print(nums[i])
            
            if nums[i] in Dict:
                Dict[nums[i]]+=1
            else:
                Dict[nums[i]]=1
        return ans