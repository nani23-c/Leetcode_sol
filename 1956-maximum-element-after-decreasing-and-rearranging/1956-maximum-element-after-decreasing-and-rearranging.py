class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        temp=1
        for i in range(1,n):
            if arr[i]>temp:
                temp +=1
        return temp
        