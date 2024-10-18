class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        if n == 0:
            return ""

        comp = []
        i = 0

        while i < n:
            c = word[i]
            count = 0

            while i < n and word[i] == c and count < 9:
                i += 1
                count += 1
            
            comp.append(f"{count}{c}")

        return "".join(comp)