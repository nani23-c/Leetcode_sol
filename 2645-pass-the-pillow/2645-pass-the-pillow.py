class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        temp = True
        k = 1
        while(time !=0):
            if temp is True:
                k += 1
            if temp is False:
                k -=1 
            time -=1 
            if k==n:
                temp = False
            if k==1:
                temp = True 
        return k
            