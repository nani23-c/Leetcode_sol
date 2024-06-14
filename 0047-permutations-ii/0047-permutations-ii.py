class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       out=permutations(nums)
       out = set(out)
       return out
        