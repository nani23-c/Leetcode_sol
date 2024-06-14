class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr and curr.next:
            next_pair = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = next_pair
            prev = curr
            curr = next_pair
        
        return dummy.next

            
            