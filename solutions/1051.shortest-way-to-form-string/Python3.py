class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        count = 0
        i = 0
        
        while i < len(target):
            if target[i] not in source_set:
                return -1
            j = 0
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                j += 1
            count += 1
        
        return count