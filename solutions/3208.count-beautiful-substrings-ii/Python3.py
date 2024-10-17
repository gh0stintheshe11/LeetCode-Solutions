k0 = [i for i in range(1001)]
for a in reversed(range(2, len(k0))):
    a2 = a*a
    for i in range(a2, len(k0), a2):
        if k0[i]==i:
            k0[i] //= a

vowels = "aeiou"

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        counter = {0: {0: 1}}
        total = 0
        vowel_cnt = 0
        k = k0[k]
        
        for i, ch in enumerate(s, 1):
            if ch in vowels:
                vowel_cnt += 1
            diff = i-2*vowel_cnt
            idx = vowel_cnt % k
            if diff in counter:
                d = counter[diff]
                total += d.get(idx % k, 0)
                if idx not in d:
                    d[idx] = 1
                else:
                    d[idx] += 1
            else:
                counter[diff] = {idx: 1} 
            
        return total