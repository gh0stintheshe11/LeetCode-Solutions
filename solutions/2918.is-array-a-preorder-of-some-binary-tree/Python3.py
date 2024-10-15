class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if not nodes:
            return True
        
        stack = []
        index = 0

        stack.append(nodes[0][0])  # Start with the root node
        for node in nodes[1:]:
            current_id, parent_id = node
            
            while stack and stack[-1] != parent_id:
                stack.pop()

            if not stack:
                return False

            stack.append(current_id)

        return True