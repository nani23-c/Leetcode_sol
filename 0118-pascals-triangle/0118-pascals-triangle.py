class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        a.append(1)

        for i in range(1,numRows+1):
            k=i*a[i-1]
            a.append(k)

        def factorian(m,k):
            h=int(a[m]/(a[m-k]*a[k]))
            return h
        b=[]
        for i in range(numRows):
            c=[]
            for j in range(i+1):
                c.append(factorian(i,j))
            b.append(c)
                
        return b