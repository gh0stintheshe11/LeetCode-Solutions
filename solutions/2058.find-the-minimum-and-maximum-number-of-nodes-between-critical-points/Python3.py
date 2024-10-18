# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        critical_points = []
        idx = 1
        prev, curr, nxt = head, head.next, head.next.next

        while nxt:
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical_points.append(idx)
            
            prev = curr
            curr = nxt
            nxt = nxt.next
            idx += 1
        
        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        max_distance = critical_points[-1] - critical_points[0]

        return [min_distance, max_distance]