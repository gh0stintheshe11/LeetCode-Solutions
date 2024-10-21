# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitCircularLinkedList(self, list: ListNode) -> List[ListNode]:
        if not list:
            return [None, None]
        
        # Calculate the length of the circular linked list
        current = list
        length = 1
        while current.next != list:
            length += 1
            current = current.next

        # Determine size of each half
        first_half_size = (length + 1) // 2
        second_half_size = length - first_half_size
        
        # Split the first half
        first_half_head = list
        prev = None
        current = list
        for _ in range(first_half_size):
            prev = current
            current = current.next
        prev.next = first_half_head  # Making first half circular

        # Split the second half
        second_half_head = current
        prev = None
        for _ in range(second_half_size):
            prev = current
            current = current.next
        prev.next = second_half_head  # Making second half circular
        
        return [first_half_head, second_half_head]