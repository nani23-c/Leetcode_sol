class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        a=list(a)
        b=set(nums2)
        b=list(b)
        c=[]
        for i in range(len(a)):
            if a[i]  in b:
                c.append(a[i])
        return c