class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word):
            if len(word) != len(pattern):
                return False
            p_to_w, w_to_p = {}, {}
            for p_char, w_char in zip(pattern, word):
                if p_char in p_to_w and p_to_w[p_char] != w_char:
                    return False
                if w_char in w_to_p and w_to_p[w_char] != p_char:
                    return False
                p_to_w[p_char] = w_char
                w_to_p[w_char] = p_char
            return True
        
        return [word for word in words if matches(word)]