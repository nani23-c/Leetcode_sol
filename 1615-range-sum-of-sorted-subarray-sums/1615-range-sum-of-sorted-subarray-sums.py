class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        for i in range(1,n):
            nums[i]+=nums[i-1]
        ans = []
        for i in range(1,n):
            for j in range(i):
                ans.append(nums[i]-nums[j])
        ans+=nums
        ans = [0]+ans
        ans.sort()
        return sum(ans[left:right+1])%(10**9+7)

            