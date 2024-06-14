class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums  = heights.copy()
        nums.sort()
        count = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] != heights[i]:
                count+=1 
        return count
        