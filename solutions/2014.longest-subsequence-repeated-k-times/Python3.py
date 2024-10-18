class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s: freq[ord(ch)-97] += 1
        
        cand = [chr(i+97) for i, x in enumerate(freq) if x >= k] # valid candidates 
        
        def fn(ss): 
            """Return True if ss is a k-repeated sub-sequence of s."""
            i = cnt = 0
            for ch in s: 
                if ss[i] == ch: 
                    i += 1
                    if i == len(ss): 
                        if (cnt := cnt + 1) == k: return True  
                        i = 0
            return False 
        
        ans = ""
        queue = deque([""])
        while queue: 
            x = queue.popleft()
            for ch in cand:  
                xx = x + ch
                if fn(xx): 
                    ans = xx
                    queue.append(xx)
        return ans