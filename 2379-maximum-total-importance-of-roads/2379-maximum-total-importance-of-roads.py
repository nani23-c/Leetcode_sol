class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        imp = [0 for i in range(n)]
        ans = 0
        for i in roads:
            imp[i[0]]+=1
            imp[i[1]]+=1
        imp.sort()
        temp = [i for i in range(1,n+1)]
        for i in range(n):
            ans += temp[i]*imp[i]
        return ans

        