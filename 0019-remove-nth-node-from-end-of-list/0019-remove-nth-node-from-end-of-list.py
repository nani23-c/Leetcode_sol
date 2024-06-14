# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        count = 0
        while cur is not None:
            count += 1 
            cur = cur.next 
        count = count-n 
        if count ==0:
            return head.next 
        cur = head 
        for i in range(count-1):
            cur = cur.next
        cur.next = cur.next.next 
        return head

    
        