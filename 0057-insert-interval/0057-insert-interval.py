class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        intervals.sort()
        arr = [0]*n
        for i in range(1,n):
            if intervals[i][0]<=intervals[i-1][1]:
                arr[i-1]=1
                intervals[i][0]=intervals[i-1][0]
                intervals[i][1]=max(intervals[i-1][1],intervals[i][1])
                
        ans = []
        for i in range(n):
            if arr[i]==0:
                ans.append(intervals[i])
        return ans
                


        