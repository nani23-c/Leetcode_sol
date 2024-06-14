class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val in nums:
            flag = True 
        else:
            flag = False 
        while(flag):
            nums.pop(nums.index(val))
            if val not in nums:
                flag = False
        return len(nums)

        