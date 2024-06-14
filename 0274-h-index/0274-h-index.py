class Solution:
    def hIndex(self, citations: List[int]) -> int:
        k = 0
        n = len(citations)
        for i in range(n+1):
            cur = 0 
            for j in range(n):
                if citations[j]>=i:
                    cur +=1
            if cur>=i:
                k = i
            else:
                break 
        return k 


        