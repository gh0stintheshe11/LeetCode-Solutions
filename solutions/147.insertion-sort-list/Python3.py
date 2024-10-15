# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # A dummy head for the sorted part
        curr = head  # The current node to be inserted into the sorted part
        
        while curr:
            prev = dummy  # Start at the beginning of the sorted part
            # Find the right place to insert curr
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_temp = curr.next  # Save the next node to be processed
            # Insert curr to the sorted part
            curr.next = prev.next
            prev.next = curr
            
            curr = next_temp  # Move to the next node
        
        return dummy.next