class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
            nums.sort()
            n = len(nums)
            prev = nums[0]
            count = 0 
            for i in range(1,n):
                if nums[i]<=prev:
                    prev +=1 
                    count+= prev-nums[i]
                else:
                  prev = nums[i]
            return count