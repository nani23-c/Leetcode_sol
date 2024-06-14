class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        b=[]
        for i in range(len(nums)):
            a=nums[i]
            nums.pop(i)
            if a not in nums:
                b.append(a)

            nums.insert(i,a)
        return sum(b)
