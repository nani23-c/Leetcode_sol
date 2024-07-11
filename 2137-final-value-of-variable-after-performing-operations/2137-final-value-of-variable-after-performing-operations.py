class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        an = 0 
        for i in range(n):
            if operations[i][0]=="+" or  operations[i][-1]=="+" :
                an +=1 
            else:
                an-=1
        return an
