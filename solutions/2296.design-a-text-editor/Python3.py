class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class TextEditor:

    def __init__(self):
        self.dummy = Node()
        self.cursor = self.dummy

    def addText(self, text: str) -> None:
        _next = self.cursor.next
        for c in text:
            self.cursor.next = Node(val=c)
            self.cursor.next.prev = self.cursor
            self.cursor = self.cursor.next
        self.cursor.next = _next
        if _next:
            _next.prev = self.cursor

    def deleteText(self, k: int) -> int:
        ans = 0
        _next = self.cursor.next
        while ans < k and self.cursor.val:
            self.cursor = self.cursor.prev
            ans += 1
        self.cursor.next = _next
        if _next:
            _next.prev = self.cursor
        return ans      

    def cursorLeft(self, k: int) -> str:
        i = 0
        while i < k and self.cursor.prev:
            self.cursor = self.cursor.prev
            i += 1
        ans = []
        temp = self.cursor
        j = 0
        while j < 10 and temp.val:
            ans.append(temp.val)
            temp = temp.prev
            j += 1
        return ''.join(ans[::-1])

    def cursorRight(self, k: int) -> str:
        i = 0
        while i < k and self.cursor.next:
            self.cursor = self.cursor.next
            i += 1
        ans = []
        temp = self.cursor
        j = 0
        while j < 10 and temp.val:
            ans.append(temp.val)
            temp = temp.prev
            j += 1
        return ''.join(ans[::-1])