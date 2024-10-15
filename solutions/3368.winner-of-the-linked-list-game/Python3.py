# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd_points = 0
        even_points = 0
        
        current = head
        
        while current and current.next:
            if current.val > current.next.val:
                even_points += 1
            else:
                odd_points += 1
            # Move to the next pair
            current = current.next.next
        
        if odd_points > even_points:
            return "Odd"
        elif even_points > odd_points:
            return "Even"
        else:
            return "Tie"