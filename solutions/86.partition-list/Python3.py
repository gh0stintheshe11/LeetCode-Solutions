class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeHead = ListNode(0)
        before = beforeHead
        afterHead = ListNode(0)
        after = afterHead
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None
        before.next = afterHead.next
        
        return beforeHead.next