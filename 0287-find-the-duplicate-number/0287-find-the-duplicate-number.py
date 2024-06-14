class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicti={}
        for i in nums:
            if i in dicti:
                return i 
            else:
                dicti[i]=True
        