class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i=1
      k=len(list(set(nums)))
      while(len(nums) != k):
        if nums[i]==nums[i-1]:
          nums.pop(i)
        else:
          i=i+1
      return k
        