class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(map(len, words)) > len(result): return False 
        
        words.append(result)
        digits = [0]*10 
        mp = {} 
        
        def fn(i, j, val): 
            if j == len(result): return val == 0 
            if i == len(words): return val % 10 == 0 and fn(0, j+1, val//10)
            
            if j >= len(words[i]): return fn(i+1, j, val)
            if words[i][~j] in mp: 
                if j and j+1 == len(words[i]) and mp[words[i][~j]] == 0: return 
                if i+1 == len(words): return fn(i+1, j, val - mp[words[i][~j]])
                else: return fn(i+1, j, val + mp[words[i][~j]])
            else: 
                for k, x in enumerate(digits): 
                    if not x and (k or j == 0 or j+1 < len(words[i])): 
                        mp[words[i][~j]] = k
                        digits[k] = 1
                        if i+1 == len(words) and fn(i+1, j, val-k): return True 
                        if i+1 < len(words) and fn(i+1, j, val+k): return True 
                        digits[k] = 0
                        mp.pop(words[i][~j])
        
        return fn(0, 0, 0)