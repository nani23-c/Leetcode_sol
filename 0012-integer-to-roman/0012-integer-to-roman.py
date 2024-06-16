class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        thousands = ["M","MM","MMM"]
        hundreds  = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["I","II","III","IV","V","VI","VII","VIII","IX"]
        temp = num-num%1000
        a=temp//1000
        num = num%1000
        if a>0:
            ans = ans + thousands[a-1]
        temp = num-num%100
        a = temp//100
        num = num%100
        if a>0:
            ans += hundreds[a-1]
        temp = num-num%10
        a = temp//10
        num = num%10
        if a>0:
            ans += tens[a-1]
        if num>0:
            ans += ones[num-1]
        return ans
        
        
        
       
            
        
