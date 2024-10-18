class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        
        rules = defaultdict(list)
        for a in allowed:
            rules[a[:2]].append(a[2])
        
        def can_build(current):
            if len(current) == 1:
                return True
            for i in range(len(current) - 1):
                if current[i:i+2] not in rules:
                    return False
            
            def build_next_level(current, next_level, idx):
                if idx == len(current) - 1:
                    return can_build(next_level)
                for char in rules[current[idx:idx+2]]:
                    if build_next_level(current, next_level + char, idx + 1):
                        return True
                return False
            
            return build_next_level(current, "", 0)
        
        return can_build(bottom)