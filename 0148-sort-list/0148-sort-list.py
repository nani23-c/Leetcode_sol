# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        temp = head
        while(temp):
            ans.append(temp.val)
            temp = temp.next
        ans.sort()
        temp = head
        i = 0 
        while(temp):
            temp.val = ans[i]
            temp= temp.next 
            i+=1 
        return head
        