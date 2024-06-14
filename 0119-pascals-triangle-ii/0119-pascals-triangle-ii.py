class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        numRows=rowIndex
        a.append(1)

        for i in range(1,numRows+1):
            k=i*a[i-1]
            a.append(k)

        def factorian(m,k):
            h=int(a[m]/(a[m-k]*a[k]))
            return h
        
        for i in range(numRows+1):
            if(i==numRows):
                c=[]
                for j in range(i+1):
                   c.append(factorian(i,j))
                return c
        