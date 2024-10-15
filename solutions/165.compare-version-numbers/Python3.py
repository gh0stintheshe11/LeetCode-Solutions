class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        len1, len2 = len(v1), len(v2)
        
        for i in range(max(len1, len2)):
            rev1 = v1[i] if i < len1 else 0
            rev2 = v2[i] if i < len2 else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1

        return 0