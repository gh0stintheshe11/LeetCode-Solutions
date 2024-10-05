class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        pred = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next 
            head = head.next
        return dummy.next