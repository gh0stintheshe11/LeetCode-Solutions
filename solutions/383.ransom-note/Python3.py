class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        for char, count in ransom_counter.items():
            if magazine_counter[char] < count:
                return False
        return True