class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        for i in range(1,n):
            arr[i]=arr[i]^arr[i-1]
        ans = []
        for i in queries:
            if i[0]==0:
                ans.append(arr[i[1]])
            else:
                ans.append(arr[i[1]]^arr[i[0]-1])
        return ans
