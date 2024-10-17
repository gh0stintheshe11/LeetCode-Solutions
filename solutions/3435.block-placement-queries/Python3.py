from typing import List

class Node:
    def __init__(self, flag=True, node=None):
        if flag:
            self.left = None
            self.right = None
            self.lval = 0
            self.rval = 0
            self.bestval = 0
            self.connected = True
        else:
            self.left = node.left
            self.right = node.right
            self.lval = node.lval
            self.rval = node.rval
            self.bestval = node.bestval
            self.connected = node.connected
            
def Build(l, r, arr):
    if l == r:
        return Node()
    mid = (l + r) // 2
    lnode = Build(l, mid, arr)
    rnode = Build(mid + 1, r, arr)
    node = Node()
    node.left = lnode
    node.right = rnode
    node.bestval = lnode.bestval + rnode.bestval + 1
    node.lval = node.bestval
    node.rval = node.bestval
    return node

def update(l, r, idx, node):
    if l > r:
        return
    mid = (l + r) // 2
    if l == r == idx:
        node.connected = False
        node.lval = 0
        node.rval = 0
        node.bestval = 0
        return
    if l <= idx <= mid:
        update(l, mid, idx, node.left)
    elif mid + 1 <= idx <= r:
        update(mid + 1, r, idx, node.right)
    else:
        return
    lnode = node.left
    rnode = node.right
    if lnode.connected and rnode.connected:
        node.bestval = lnode.bestval + rnode.bestval + 1
        node.lval = node.bestval
        node.rval = node.bestval
    elif lnode.connected:
        node.bestval = max(lnode.bestval + rnode.lval + 1, rnode.bestval)
        node.lval = lnode.bestval + rnode.lval + 1
        node.rval = rnode.rval
    elif rnode.connected:
        node.bestval = max(lnode.bestval, lnode.rval + rnode.bestval + 1)
        node.lval = lnode.lval
        node.rval = lnode.rval + rnode.bestval + 1
    else:
        node.bestval = max(lnode.bestval, rnode.bestval, lnode.rval + rnode.lval + 1)
        node.lval = lnode.lval
        node.rval = rnode.rval
    node.connected = False

def query(l, r, idx, hnode):
    if l > r or idx < l:
        nnode = Node()
        nnode.bestval = -1
        nnode.lval = -1
        nnode.rval = -1
        return nnode
    mid = (l + r) // 2
    if idx >= r:
        return Node(False, hnode)
    if l <= idx <= r:
        mid = (l + r) // 2
        lnode = query(l, mid, idx, hnode.left)
        rnode = query(mid + 1, r, idx, hnode.right)
        node = Node()
        if lnode.connected and rnode.connected:
            node.bestval = lnode.bestval + rnode.bestval + 1
            node.lval = node.bestval
            node.rval = node.bestval
        elif lnode.connected:
            node.bestval = max(lnode.bestval + rnode.lval + 1, rnode.bestval)
            node.lval = lnode.bestval + rnode.lval + 1
            node.rval = rnode.rval
        elif rnode.connected:
            node.bestval = max(lnode.bestval, lnode.rval + rnode.bestval + 1)
            node.lval = lnode.lval
            node.rval = lnode.rval + rnode.bestval + 1
        else:
            node.bestval = max(lnode.bestval, rnode.bestval, lnode.rval + rnode.lval + 1)
            node.lval = lnode.lval
            node.rval = rnode.rval
        node.connected = False
        return node

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ans = []
        arr = max([i[1] for i in queries]) + 1
        head = Build(0, arr - 1, arr)
        for curr in queries:
            if curr[0] == 1:
                x = curr[1]
                temp = head
                update(0, arr - 1, x, temp)
            else:
                x, sz = curr[1], curr[2]
                temp = head
                nnode = query(0, arr - 1, x, temp)
                ans.append(nnode.bestval >= sz)
                
        return ans