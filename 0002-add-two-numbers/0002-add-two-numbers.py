# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None 
        carry = 0 
        while(l1 is not None and l2 is not None):
            temp = carry + l2.val + l1.val
            if temp>9:
                temp -= 10
                carry = 1 
            else:
                carry = 0 
            if head is None: 
                head = ListNode(temp) 
                cur = head 
            else:
                cur.next =  ListNode(temp)
                cur = cur.next
            l1 = l1.next 
            l2 = l2.next
        while(l1 is not None):
            temp = carry+l1.val
            if temp>9:
                temp -= 10
                carry = 1 
            else:
                carry = 0
            cur.next =  ListNode(temp)
            cur = cur.next
            l1=l1.next
        while(l2 is not None):
            temp = carry+l2.val
            if temp>9:
                temp -= 10
                carry = 1 
            else:
                carry = 0
            cur.next =  ListNode(temp)
            cur = cur.next
            l2=l2.next
        if carry ==1:
            cur.next = ListNode(carry)
        return head
            

            