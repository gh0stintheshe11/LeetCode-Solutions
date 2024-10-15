class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def RLE(S):
            groups = []
            lengths = []
            prev = ''
            count = 0
            for c in S:
                if c == prev:
                    count += 1
                else:
                    if prev:
                        groups.append(prev)
                        lengths.append(count)
                    prev = c
                    count = 1
            groups.append(prev)
            lengths.append(count)
            return groups, lengths
        
        s_groups, s_lengths = RLE(s)
        valid_count = 0

        for word in words:
            w_groups, w_lengths = RLE(word)
            if s_groups != w_groups:
                continue
            is_valid = True
            for sl, wl in zip(s_lengths, w_lengths):
                if sl < wl or (sl < 3 and sl != wl):
                    is_valid = False
                    break
            if is_valid:
                valid_count += 1
        
        return valid_count