class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_map = {}
        result = []
        
        for name in names:
            if name not in name_map:
                result.append(name)
                name_map[name] = 0
            else:
                k = name_map[name] + 1
                new_name = f"{name}({k})"
                
                while new_name in name_map:
                    k += 1
                    new_name = f"{name}({k})"
                
                result.append(new_name)
                name_map[name] = k
                name_map[new_name] = 0
        
        return result