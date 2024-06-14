class Solution:
    def reverse(self, x: int) -> int:
        h=0
        a=abs(x)
        if(a==0):
            return 0
        s=''
        while(a>0):
            i=a%10
            s=s+str(i)
            a=int(a/10)
        if(x>0):
             h=int(s)
        else:
            h= -1*int(s)
        if(h<-1*pow(2,31) or h>pow(2,31)-1):
            return 0
        else:
            return h