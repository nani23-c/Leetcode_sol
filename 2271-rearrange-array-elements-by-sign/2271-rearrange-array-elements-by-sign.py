class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = []
        b = []
        ans = []
        for i in range(n):
            if nums[i]>0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        for i in range(n//2):
            ans.append(a[i])
            ans.append(b[i])
        return ans
        