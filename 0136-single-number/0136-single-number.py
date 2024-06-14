class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti = {}
        for i in nums:
            dicti[i] = 0
        for i in nums:
            dicti[i] += 1
        for i in nums:
            if dicti[i] == 1:
                return i

        