class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       nums3=[]
       while(len(nums1)+len(nums2)!=0)    :
           if len(nums1) !=0 and len(nums2)!=0:
                if nums1[0]> nums2[0]:
                   nums3.append(nums2.pop(0))  
                else:
                    nums3.append(nums1.pop(0))
           else:
                if len(nums1) ==0:
                    nums3 = nums3+nums2
                    nums2=[]
                if len(nums2)==0:
                    nums3 = nums3+nums1
                    nums1=[]
       n = len(nums3)
       if n%2 == 0:
           return (nums3[n//2]+nums3[n//2-1])/2
       else:
           return nums3[n//2]