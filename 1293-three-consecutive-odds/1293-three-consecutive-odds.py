class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        if arr[0]%2==1:
            prev1 = True 
        else:
            prev1 = False
        if arr[1]%2==1:
            prev2 = True 
        else:
            prev2 = False
        if arr[2]%2==1:
            prev3 = True 
        else:
            prev3 = False
        if prev1 and prev2 and prev3:
            return True
        for i in range(3,n):
            prev1 = prev2
            prev2 = prev3
            if arr[i]%2==1:
                prev3 = True 
            else:
                prev3 = False 
            if prev1 and prev2 and prev3:
                return True 
        return False
            
        

        
        