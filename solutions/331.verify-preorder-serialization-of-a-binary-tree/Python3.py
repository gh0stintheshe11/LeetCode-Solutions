class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        nodes = preorder.split(',')
        
        for node in nodes:
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        
        return slots == 0