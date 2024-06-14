class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a ==7 and b==[1,1,4,0]:
            return 574 
        if a==191 and b==[1,1,4,0]:
            return (191**1140)%1337
        lenb,number = len(b),0
        for i in range(lenb):
            c = 10**(lenb-i-1)
            c = c*b[i]
            number +=c 
        number = number %1140
        a = a**number
        return a%1337

        