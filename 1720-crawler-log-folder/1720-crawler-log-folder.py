class Solution:
    def minOperations(self, logs: List[str]) -> int:
        temp = 0 
        n = len(logs)
        for i in range(n):
            if logs[i]=="../":
                if temp!=0:
                    temp -=1
            elif logs[i][-2]==".":
                temp = temp
            else:
                temp +=1
        return temp