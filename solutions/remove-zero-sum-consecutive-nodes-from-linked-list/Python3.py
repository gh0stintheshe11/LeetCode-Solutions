# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_map = {0: dummy}
        
        current = head
        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_map:
                to_remove = prefix_map[prefix_sum].next
                sum_in_between = prefix_sum
                while to_remove != current:
                    sum_in_between += to_remove.val
                    if sum_in_between in prefix_map:
                        del prefix_map[sum_in_between]
                    to_remove = to_remove.next
                prefix_map[prefix_sum].next = current.next
            else:
                prefix_map[prefix_sum] = current
            current = current.next
        
        return dummy.next