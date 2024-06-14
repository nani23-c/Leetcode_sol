class Solution:
    def romanToInt(self, s: str) -> int:
       a=len(s)
       p='k'
       s=s+p
       num=0
       for i in range(a):
            if(s[i]=='I'):
                if(s[i+1]=='V' or s[i+1]=='X'):
                   num=num-1
                else:
                    num=num+1
            elif(s[i]=='X'):
                if(s[i+1]=='L' or s[i+1]=='C'):
                   num=num-10
                else:
                    num=num+10
            elif(s[i]=='C'):
                if(s[i+1]=='D' or s[i+1]=='M'):
                   num=num-100
                else:
                    num=num+100
            elif(s[i]=='V'):
                num=num+5
            elif(s[i]=='L'):
                 num=num+50
            elif(s[i]=='D'):
                 num=num+500
            elif(s[i]=='M'):
                 num=num+1000
    
       return num

              