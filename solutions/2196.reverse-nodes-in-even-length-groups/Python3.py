# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        group_size = 1

        while current:
            # Determine how many nodes are left
            count = 0
            node = current
            while node and count < group_size:
                node = node.next
                count += 1

            # If the group has even length, reverse it
            if count % 2 == 0:
                prev.next = self.reverse(current, count)

            # Move prev to end of current group
            while count > 0:
                prev = prev.next
                count -= 1

            # Move to next group
            current = prev.next
            group_size += 1

        return dummy.next

    def reverse(self, head: ListNode, k: int) -> ListNode:
        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head.next = current
        return prev