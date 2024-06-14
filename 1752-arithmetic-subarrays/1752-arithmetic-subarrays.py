class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def Find(a,b):
            if a==b:
                return True
            temp = nums[a:b+1]
            temp.sort()
            h = temp[1]-temp[0]
            for i in range(b-a):
                if temp[i+1]-temp[i] != h:
                    return False 
            return True


        m = len(l)
        Boolean = []
        for i in range(m):
            Boolean.append(Find(l[i],r[i]))
        return Boolean

        