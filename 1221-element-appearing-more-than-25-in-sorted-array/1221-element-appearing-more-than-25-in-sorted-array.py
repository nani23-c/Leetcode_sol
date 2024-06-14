class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        n = len(arr)
        k = n/4 
        count = 1
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                count +=1 
                if count>k:
                    return arr[i]
            else:
                count = 1

        