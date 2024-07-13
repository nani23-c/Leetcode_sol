# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head.val == 0:
            ans = 0 
        else:
            ans = 1
        head = head.next
        while(head):
            ans = ans*2
            if head.val==1:
                ans +=1 
            head = head.next
        return ans

        