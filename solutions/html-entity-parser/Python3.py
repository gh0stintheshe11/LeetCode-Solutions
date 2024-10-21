class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        i = 0
        n = len(text)
        result = []
        
        while i < n:
            if text[i] == '&':
                # Try to find an entity by looking ahead
                for e in entities:
                    if text.startswith(e, i):
                        result.append(entities[e])
                        i += len(e)
                        break
                else:
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1
                
        return ''.join(result)