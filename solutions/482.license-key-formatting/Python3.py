class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        size = len(s)
        first_group_size = size % k
        parts = []
        
        if first_group_size > 0:
            parts.append(s[:first_group_size])
        
        for i in range(first_group_size, size, k):
            parts.append(s[i:i+k])
        
        return '-'.join(parts)