class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        
        for word in words:
            start = s.find(word)
            while start != -1:
                end = start + len(word)
                for i in range(start, end):
                    bold[i] = True
                start = s.find(word, start + 1)
        
        result = []
        i = 0
        while i < n:
            if bold[i]:
                result.append("<b>")
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)