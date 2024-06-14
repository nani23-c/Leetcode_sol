class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            index = i 
            while (index>0 and nums[index]<nums[index-1]):
                nums[index-1],nums[index]= nums[index],nums[index-1]
                index -=1 
                print(nums)
        
        
        