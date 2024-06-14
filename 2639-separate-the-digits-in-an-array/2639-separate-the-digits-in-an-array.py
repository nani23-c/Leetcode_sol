class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            n=i
            k=[]
            if(n>9):
                while(n>0):
                    b=n%10
                    k.append(b)
                    n=n//10
            else:
                k.append(i)
            k.reverse()
            for c in k:
                a.append(c)
        return a
