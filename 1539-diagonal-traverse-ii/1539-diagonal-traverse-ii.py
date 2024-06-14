class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            h = len(nums[i])
            if h >n:
                n = h 
        memory = [[]for i in range(m+n)]
        for i in range(m):
            for j in range(len(nums[i])):
                memory[i+j].append(nums[i][j])
        out = []
        for i in range(m+n):
            k = len(memory[i])
            for j in range(k-1,-1,-1):
                out.append(memory[i][j])
        return out
       