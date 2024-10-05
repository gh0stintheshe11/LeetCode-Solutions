class Node:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_count = {}
        self.count_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] += 1
            self.count_map[count].keys.remove(key)
            
            new_count = count + 1
            if new_count not in self.count_map:
                new_node = Node()
                self.count_map[new_count] = new_node
                self._add_node_after(new_node, self.count_map[count])
            self.count_map[new_count].keys.add(key)
            
            if not self.count_map[count].keys:
                self._remove_node(self.count_map[count])
                del self.count_map[count]
        else:
            self.key_count[key] = 1
            if 1 not in self.count_map:
                new_node = Node()
                self.count_map[1] = new_node
                self._add_node_after(new_node, self.head)
            self.count_map[1].keys.add(key)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        self.key_count[key] -= 1
        self.count_map[count].keys.remove(key)
        
        if self.key_count[key] == 0:
            del self.key_count[key]
        else:
            new_count = count - 1
            if new_count not in self.count_map:
                new_node = Node()
                self.count_map[new_count] = new_node
                self._add_node_after(new_node, self.count_map[count].prev)
            self.count_map[new_count].keys.add(key)
        
        if not self.count_map[count].keys:
            self._remove_node(self.count_map[count])
            del self.count_map[count]

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()