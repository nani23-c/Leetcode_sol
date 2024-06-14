class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        carry = 0 
        ans = ""
        if n>m:
            extra = ""
            for i in range(n-m):
                extra += "0"
            num2 = extra +num2
        else:
            extra = ""
            for i in range(m-n):
                extra += "0" 
            num1 = extra+num1
        n = max(n,m)
        carry = 0 
        ans = ""
        for i in range(n-1,-1,-1):
            a = int(num1[i])
            b = int(num2[i])
            temp = a+b+carry
            if temp > 9:
                temp -=10
                carry = 1
            else:
                carry = 0
            ans = str(temp)+ans
        if carry==1:
            ans = "1"+ans 
        return ans

                

