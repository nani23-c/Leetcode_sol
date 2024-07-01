class Solution:
    def isHappy(self, n: int) -> bool:
        while(n>9):
            temp = 0
            while(n>0):
                temp += (n%10)**2
                n = n//10 
            if temp==1:
                return True 
            n = temp
        if n==1 or n==7:
            return True
        else:
            return False
        