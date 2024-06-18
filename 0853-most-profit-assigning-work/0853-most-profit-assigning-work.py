class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)
        temp = []
        for i in range(n):
            temp.append([difficulty[i],profit[i]])
        temp.sort()
        for i in range(1,n):
            temp[i][1]=max(temp[i][1],temp[i-1][1])
        worker.sort()
        j = 0 
        ans = 0
        nani = 0
        for i in range(m):
            while (j<n) and temp[j][0]<=worker[i]:
                    nani = max(nani,temp[j][1])
                    j = j+1
            ans = ans+nani 
        return ans
                    