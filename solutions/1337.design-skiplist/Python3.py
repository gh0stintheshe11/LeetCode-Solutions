import random

class ListNode: 
    def __init__(self, val, cnt=1, next=None, down=None): 
        self.val = val
        self.cnt = cnt
        self.next = next
        self.down = down
        
class Skiplist:

    def __init__(self):
        self.head = ListNode(-float('inf'))
        self.p = 1/4 
            
    def search(self, target: int) -> bool:
        node = self.head 
        while node and node.val < target: 
            if node.next and node.next.val <= target: 
                node = node.next 
            else: 
                node = node.down 
        return node and node.val == target

    def add(self, num: int) -> None:
        node = self.head 
        stack = []
        while node and node.val <= num: 
            if node.next and node.next.val <= num: 
                node = node.next 
            else: 
                stack.append(node)
                node = node.down
        if node and node.val == num: 
            while node: 
                node.cnt += 1
                node = node.down 
        else: 
            prev = None
            while True: 
                if stack: 
                    node = stack.pop()
                    node.next = prev = ListNode(num, down=prev, next=node.next)
                else: 
                    self.head = ListNode(-float('inf'), down=self.head)
                    self.head.next = prev = ListNode(num, down=prev)
                if random.random() >= self.p: 
                    break 

    def erase(self, num: int) -> bool:
        node = self.head 
        stack = []
        ans = False
        while node: 
            if node.next and node.next.val < num: 
                node = node.next
            else: 
                stack.append(node)
                node = node.down 
        while stack: 
            node = stack.pop()
            if node.next and node.next.val == num: 
                ans = True
                if node.next.cnt > 1: 
                    node.next.cnt -= 1
                else: 
                    node.next = node.next.next 
            else: 
                break 
        return ans