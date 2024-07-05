# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        cur = head
        curval = head.val
        cur = cur.next
        len1 = 1
        while(cur.next):
            temp = cur.next
            if cur.val>curval and cur.val>temp.val:
                ans.append(len1)
            if cur.val<curval and cur.val<temp.val:
                ans.append(len1)
            curval = cur.val 
            cur = cur.next 
            len1 +=1
        if len(ans)<2:
            return [-1,-1]
        else:
            print(ans)
            a = len(ans)
            m = ans[-1]
            for i in range(1,a):
                m = min((ans[i]-ans[i-1]),m)
            M = max(ans)-min(ans)
            return [m,M]

            

        