# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # To handle edge cases smoothly
        tail = dummy
        current = head.next  # Skip the first zero
        sum_between_zeros = 0
        
        while current:
            if current.val == 0:
                # End of a segment, append the accumulated sum to the new list
                tail.next = ListNode(sum_between_zeros)
                tail = tail.next
                sum_between_zeros = 0
            else:
                # Accumulate values
                sum_between_zeros += current.val
            current = current.next
        
        return dummy.next