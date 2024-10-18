class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a list of tuples with the information of the replacements
        changes = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        last_index = 0
        
        for i, src, tgt in changes:
            if s[i:i + len(src)] == src:
                result.append(s[last_index:i])
                result.append(tgt)
                last_index = i + len(src)
        
        result.append(s[last_index:])
        return ''.join(result)