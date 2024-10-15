class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 3
            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i+2:j]
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i = j + 1
            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i+1:j]
                if not 1 <= len(tagname) <= 9 or not all(c.isupper() for c in tagname):
                    return False
                stack.append(tagname)
                i = j + 1
            else:
                i += 1
        return not stack