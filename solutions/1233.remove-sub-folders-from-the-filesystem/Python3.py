class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = None
        
        for f in folder:
            if prev is None or not f.startswith(prev + '/'):
                result.append(f)
                prev = f
        
        return result