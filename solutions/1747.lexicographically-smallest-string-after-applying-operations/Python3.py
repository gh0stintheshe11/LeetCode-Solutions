class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque
        
        def add_operation(s):
            chars = list(s)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            return ''.join(chars)
        
        def rotate_operation(s, b):
            return s[-b:] + s[:-b]
        
        queue = deque([s])
        visited = set([s])
        smallest = s
        
        while queue:
            current = queue.popleft()
            
            if current < smallest:
                smallest = current
            
            added_string = add_operation(current)
            if added_string not in visited:
                visited.add(added_string)
                queue.append(added_string)
            
            rotated_string = rotate_operation(current, b)
            if rotated_string not in visited:
                visited.add(rotated_string)
                queue.append(rotated_string)
        
        return smallest