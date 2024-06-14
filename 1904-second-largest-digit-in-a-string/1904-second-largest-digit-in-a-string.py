class Solution:
    def secondHighest(self, s: str) -> int:
        a=set(s)
        b=[]
        for i in a:
            if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                b.append(int(i))
            
        if(len(b)>1):
           b.pop(b.index(max(b)))
           return max(b)
        else:
            return -1

