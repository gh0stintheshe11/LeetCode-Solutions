# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        
        n = len(elements)
        answer = [0] * n
        stack = []
        
        for i in range(n):
            while stack and elements[stack[-1]] < elements[i]:
                answer[stack.pop()] = elements[i]
            stack.append(i)
        
        return answer