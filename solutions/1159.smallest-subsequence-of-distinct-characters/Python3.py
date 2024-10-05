class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        stack = []
        seen = set()
        
        for i, ch in enumerate(s):
            if ch not in seen:
                while stack and ch < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(ch)
                seen.add(ch)
        
        return ''.join(stack)