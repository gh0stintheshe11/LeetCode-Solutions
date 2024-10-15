class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[': 
            return NestedInteger(int(s))
        
        stack, num, negative = [], None, False
        for i in range(len(s)):
            if s[i] == '-':
                negative = True
            elif s[i].isdigit():
                num = int(s[i]) if num is None else num * 10 + int(s[i])
            elif s[i] == '[':
                stack.append(NestedInteger())
            elif s[i] in ',]':
                if num is not None:
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = None, False
                if s[i] == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        
        return stack[0]