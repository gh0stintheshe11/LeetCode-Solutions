# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        in_component = False
        count = 0
        
        while head:
            if head.val in num_set:
                if not in_component:
                    count += 1
                    in_component = True
            else:
                in_component = False
            head = head.next
        
        return count