from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        def backtrack(index, path):
            if index == len(s):
                result.append(''.join(path))
                return
            if s[index] == '{':
                i = index + 1
                while s[i] != '}':
                    i += 1
                options = s[index+1:i].split(',')
                for option in options:
                    path.append(option)
                    backtrack(i + 1, path)
                    path.pop()
            else:
                path.append(s[index])
                backtrack(index + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return sorted(result)