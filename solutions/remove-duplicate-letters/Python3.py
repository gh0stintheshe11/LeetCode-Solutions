class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        added = set()
        
        for i, c in enumerate(s):
            if c in added:
                continue
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                added.remove(stack.pop())
            stack.append(c)
            added.add(c)
        
        return ''.join(stack)