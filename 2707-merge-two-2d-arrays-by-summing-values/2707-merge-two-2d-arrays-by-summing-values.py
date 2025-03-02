class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dicti = {}
        for i in nums1:
            if i[0] in dicti:
                dicti[i[0]]+=i[1]
            else:
                dicti[i[0]]=i[1]
        for i in nums2:
            if i[0] in dicti:
                dicti[i[0]]+=i[1]
            else:
                dicti[i[0]]=i[1]
        ans = []
        for i in dicti:
            ans.append([i,dicti[i]])
        ans.sort()
        return ans
        

        
        