# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        def find_parent(node, target):
            if target in node.children:
                return node
            for child in node.children:
                ans = find_parent(child, target)
                if ans: return ans
            return None

        if p in q.children:
            return root

        dummy = Node(children=[root])

        p_parent = find_parent(dummy, p)
        q_in_p = find_parent(p, q)

        p_index = p_parent.children.index(p)
        p_parent.children.pop(p_index)

        q.children.append(p)

        if q_in_p:
            q_in_p.children.remove(q)
            p_parent.children.insert(p_index, q)

        return dummy.children[0]