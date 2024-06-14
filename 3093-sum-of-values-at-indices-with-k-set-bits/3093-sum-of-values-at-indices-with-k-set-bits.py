class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0 
        for i in range(len(nums)):
            a = bin(i)
            a = a.count("1")
            if a == k:
                sum += nums[i]
        return sum
