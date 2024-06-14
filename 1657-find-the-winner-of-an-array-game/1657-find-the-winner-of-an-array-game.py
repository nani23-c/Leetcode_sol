class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_max = arr[0]
        n = k
        for i in range(1,len(arr)):
            if arr[i] > current_max:
                k = n-1
                current_max = arr[i]
            else:
                k = k-1
            if k ==0:
                return current_max
        return current_max
