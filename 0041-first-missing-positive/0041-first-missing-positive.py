class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sets = set(nums)
        i = 1
        while i in sets:
            i = i+1 
        return i
        