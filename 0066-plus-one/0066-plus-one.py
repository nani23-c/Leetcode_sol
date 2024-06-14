class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=len(digits)-1
        number=0
        for i in range(a,-1,-1):
            k=digits[a-i]
            number=number+(k*(10**i))
        number=number+1
        digit=[]
        while(number != 0):
            k=number%10
            digit.append(k)
            number=number/10
        digit.reverse()
        return digit
    
       
