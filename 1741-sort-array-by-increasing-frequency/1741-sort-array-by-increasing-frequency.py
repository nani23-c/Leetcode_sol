class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1 
        nums.sort(key = lambda x: (count[x],-x))
        return nums

        