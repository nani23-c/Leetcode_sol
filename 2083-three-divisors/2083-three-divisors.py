class Solution:
    def isThree(self, n: int) -> bool:
        a=[]
        if(n==2 or n==1 or n==0):
            return False
        for i in range(2,n):
            if(n%i==0):
                a.append(i)
            if(len(a)>1):
                return False
        if(len(a)==0):
            return False
        return True

            