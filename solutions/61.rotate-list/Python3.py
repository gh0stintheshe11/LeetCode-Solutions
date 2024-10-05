class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None

        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1

        old_tail.next = head
        
        new_tail_target_position = length - (k % length) - 1
        new_tail = head
        while new_tail_target_position > 0:
            new_tail = new_tail.next
            new_tail_target_position -= 1
        
        new_head = new_tail.next

        new_tail.next = None

        return new_head