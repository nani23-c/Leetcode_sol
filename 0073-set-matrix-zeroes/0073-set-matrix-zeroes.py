class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colums=[]

        for h in range(len(matrix)):
            i=matrix[h]
            k = len(i)
            if 0 in i:
                for j in range(k):
                    if i[j]==0 and j not in colums:
                        colums.append(j)
                matrix[h]=[0]*k
        for i in matrix:
            for j in colums:
                i[j]=0