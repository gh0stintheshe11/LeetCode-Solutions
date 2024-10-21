# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # First, determine the total length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part
        part_size, extra_parts = divmod(length, k)
        
        result = []
        current = head
        for _ in range(k):
            part_head = current
            # Each part should have an extra node if there are extra parts remaining
            size = part_size + (1 if extra_parts > 0 else 0)
            if extra_parts > 0:
                extra_parts -= 1
            
            # Create the current part
            for _ in range(size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result