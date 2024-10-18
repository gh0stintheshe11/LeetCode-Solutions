# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # Initialize three pointers
        pos_head = ListNode(0)
        neg_head = ListNode(0)
        pos_tail = pos_head
        neg_tail = neg_head

        current = head
        while current:
            if current.val >= 0:
                pos_tail.next = current
                pos_tail = pos_tail.next
            else:
                neg_tail.next = current
                neg_tail = neg_tail.next
            current = current.next

        # Terminate the lists
        pos_tail.next = None
        neg_tail.next = None

        # Now reverse the negative list
        prev = None
        current = neg_head.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Connect the reversed negative list to the positive list
        neg_head = prev
        dummy = ListNode(0)
        tail = dummy

        # Append negative list
        current = neg_head
        while current:
            tail.next = current
            tail = current
            current = current.next

        # Append positive list
        current = pos_head.next
        while current:
            tail.next = current
            tail = current
            current = current.next

        return dummy.next