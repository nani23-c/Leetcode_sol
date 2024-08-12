# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ans = []
        temp = head
        while(temp):
            ans.append(temp.val)
            temp = temp.next
        temp = True
        while(ans):
            if temp:
                head.val = ans[0]
                ans.pop(0)
                head = head.next
                temp = False
            else:
                head.val = ans[-1]
                ans.pop(-1)
                head = head.next
                temp = True
               

            

            

