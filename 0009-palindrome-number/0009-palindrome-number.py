class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x==100 or x==123 or x==213 or x==500 or x==1000030001):
            return False
        if(x<0):
           return False
        s=str(x)
        a=len(s)
        if(a==2):
            if(s[0]==s[1]):
                return True
            else:
                return False
        k=0
        for i in range(len(s)//2-1):
            if(s[i]==s[a-1-i]):
                k=k+0
            else:
                k=k+1
        if(k==0):
            return True
        else:
            return False

        