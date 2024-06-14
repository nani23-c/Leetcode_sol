class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dicti = {}
        listi = []
        for i in nums:
            if i in dicti:
                listi.append(i)
            else:
                dicti[i]=0 
        return listi


        