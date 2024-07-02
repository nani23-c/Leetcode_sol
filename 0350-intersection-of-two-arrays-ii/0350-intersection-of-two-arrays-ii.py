class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        m,n = len(nums1),len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[j]==nums2[i]:
                    ans.append(nums1[j])
                    nums1[j]='k'
                    break
        return ans